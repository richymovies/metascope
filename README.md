# MetaScope

MetaScope is a Python-based utility designed to manage and correct font issues in Windows. It ensures clear and consistent text display across applications by allowing users to list, install, and remove fonts effectively.

## Features

- **List Installed Fonts**: Display all fonts currently installed on the system.
- **Install New Fonts**: Add new fonts to the system from a specified path.
- **Remove Fonts**: Remove fonts from the system by their font name.

## Requirements

- Python 3.6 or later
- Windows Operating System

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/metascope.git
cd metascope
```

## Usage

Execute the script using Python:

```bash
python metascope.py
```

### Example Commands

- **List Fonts**: Run the script and it will automatically list all installed fonts.
- **Install Font**: Modify the script to call `install_font` with the path to a new font file.
- **Remove Font**: Modify the script to call `remove_font` with the name of the font you wish to remove.

## Notes

- The script requires administrative privileges to modify the system fonts directory and the Windows Registry.
- Be cautious when removing fonts, as this can affect system and application functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).