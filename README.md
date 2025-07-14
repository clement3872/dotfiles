# dotefiles

Personal configuration files for various machines and desktop environments.

## Structure

```
dotfiles/
├── arch-main-i3/               # Main Arch desktop with i3wm
├── arch-main-hyprland/         # Main Arch desktop with Hyprland
└── arch-idf_laptop-hyprland/   # Arch laptop with Hyprland
```

## Machine Naming Convention

`{distro}-{device}-{desktop-environment}`

- **distro**: `arch`, `manjaro`, `ubuntu`, etc.
- **device**: `main`, `laptop`, `server`, etc.
- desktop-environment: `hyprland`, `i3`, `gnome`, `kde`, etc.

## Usage

Clone the repository:
```bash
git clone https://github.com/clement3872/dotfiles.git
cd dotfiles
```

In each folder, there are configuration folders/files from the `home` directory (e.g. `~/.config/`).
