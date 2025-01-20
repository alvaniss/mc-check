<p align="center">
  <a href="https://github.com/alvaniss/mc-check"><img alt="GitHub License" src="https://img.shields.io/github/license/alvaniss/mc-check"></a>
  <a href="https://github.com/alvaniss/mc-check"><img alt="GitHub Created At" src="https://img.shields.io/github/created-at/alvaniss/mc-check"></a>
  <a href="https://github.com/alvaniss/mc-check"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/alvaniss/mc-check"></a>
</p>

## What is mc-check? ⭐

<div align="center">

  <img width="800px" src="https://raw.githubusercontent.com/alvaniss/mc-check/refs/heads/main/preview.png">

</div>

**mc-check** is a command line tool that allows you to quickly get a lot of information about the Minecraft server you need. The information you get is similar to what you see when you add a server to the server list in the game, but in a more convenient format.

## Installation 🛠️

- **Confirmed supported platforms:**
  - macOS
  - Windows
  - Linux
  
> Above are the platforms on which I have personally tested **mc-check** working. It might work on X or Y as well, I just don't know for sure.

- **Dependencies:**
  - **[python@3.9](https://www.python.org/downloads/)**
  - **[requests](https://pypi.org/project/requests/)**

### 🍎 macOS
  #### Using homebrew:
  Install [homebrew](https://brew.sh)
  ```sh
  brew tap alvaniss/mc-check https://github.com/alvaniss/mc-check
  brew update
  brew install mc-check
  ```
  #### Using pip:
  ```sh
  pip install mc-check
  ```

### 🪟 Windows
  #### Using pip:
  ```sh
  pip install mc-check
  ```

### 🐧 Linux
  #### Using pip:
  > Many Linux distros have recently switched to disabling pip, so this method may not work for your system. In that case, consider the other options listed below.
  ```sh
  pip install mc-check
  ```
  ### Using pipx:
  Install [pipx](https://pipx.pypa.io/stable/)
  ```sh
  pipx install mc-check
  ```
  #### Using Poetry:
  Install [Poetry](https://python-poetry.org/)
  ```sh
  poetry install mc-check
  ```

## Usage 💻
Checking Minecraft server with IP sp.spworlds.ru:
```sh
mc-check sp.spworlds.ru
```

## Credit ℹ️
API used for all requests is taken from [Minecraft Server Status](https://mcsrvstat.us/)
