import os
import subprocess
import ctypes
from ctypes import wintypes

class FontManager:
    def __init__(self):
        self.fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
        self.registry_path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts'

    def list_fonts(self):
        """List all fonts installed on the system."""
        fonts = os.listdir(self.fonts_dir)
        print("Installed Fonts:")
        for font in fonts:
            print(font)

    def install_font(self, font_path):
        """Install a new font from the given path."""
        try:
            font_name = os.path.basename(font_path)
            target_path = os.path.join(self.fonts_dir, font_name)
            if not os.path.exists(target_path):
                subprocess.run(['copy', font_path, self.fonts_dir], shell=True, check=True)
                self._register_font(font_name)
                print(f"Font {font_name} installed successfully.")
            else:
                print(f"Font {font_name} is already installed.")
        except Exception as e:
            print(f"Failed to install font: {e}")

    def _register_font(self, font_name):
        """Register the font in the Windows Registry."""
        try:
            key = ctypes.windll.advapi32.RegOpenKeyExW
            key.argtypes = [wintypes.HKEY, wintypes.LPCWSTR, wintypes.DWORD, wintypes.REGSAM, ctypes.POINTER(wintypes.HKEY)]
            key.restype = wintypes.LONG

            set_value = ctypes.windll.advapi32.RegSetValueExW
            set_value.argtypes = [wintypes.HKEY, wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPCVOID, wintypes.DWORD]
            set_value.restype = wintypes.LONG

            hkey = wintypes.HKEY()
            access = 0x20006  # KEY_WRITE | KEY_WOW64_64KEY
            result = key(wintypes.HKEY_LOCAL_MACHINE, self.registry_path, 0, access, ctypes.byref(hkey))
            if result == 0:  # ERROR_SUCCESS
                set_value(hkey, font_name, 0, 1, font_name.encode('utf-16le'), len(font_name.encode('utf-16le')))
                ctypes.windll.advapi32.RegCloseKey(hkey)
        except Exception as e:
            print(f"Error registering font: {e}")

    def remove_font(self, font_name):
        """Remove a font by its name."""
        try:
            font_path = os.path.join(self.fonts_dir, font_name)
            if os.path.exists(font_path):
                os.remove(font_path)
                self._unregister_font(font_name)
                print(f"Font {font_name} removed successfully.")
            else:
                print(f"Font {font_name} is not installed.")
        except Exception as e:
            print(f"Failed to remove font: {e}")

    def _unregister_font(self, font_name):
        """Unregister the font from the Windows Registry."""
        try:
            key = ctypes.windll.advapi32.RegOpenKeyExW
            key.argtypes = [wintypes.HKEY, wintypes.LPCWSTR, wintypes.DWORD, wintypes.REGSAM, ctypes.POINTER(wintypes.HKEY)]
            key.restype = wintypes.LONG

            delete_value = ctypes.windll.advapi32.RegDeleteValueW
            delete_value.argtypes = [wintypes.HKEY, wintypes.LPCWSTR]
            delete_value.restype = wintypes.LONG

            hkey = wintypes.HKEY()
            access = 0x20006  # KEY_WRITE | KEY_WOW64_64KEY
            result = key(wintypes.HKEY_LOCAL_MACHINE, self.registry_path, 0, access, ctypes.byref(hkey))
            if result == 0:  # ERROR_SUCCESS
                delete_value(hkey, font_name)
                ctypes.windll.advapi32.RegCloseKey(hkey)
        except Exception as e:
            print(f"Error unregistering font: {e}")

if __name__ == "__main__":
    fm = FontManager()
    fm.list_fonts()
    # Example usage:
    # fm.install_font('path_to_new_font.ttf')
    # fm.remove_font('name_of_installed_font.ttf')