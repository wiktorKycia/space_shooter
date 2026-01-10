# Planet Defender 🚀

A classic 2D space shooter game built with Python and Pygame, featuring multiple ships, weapons, and challenging wave-based levels.

## 🎮 Game Features

### Core Gameplay
- **Wave-Based Combat**: Fight through progressively challenging enemy waves
- **Multiple Ships**: Choose from 5 different playable ships, each with unique weapon configurations
- **Weapon Systems**: 
  - Kinetic weapons with standard projectiles
  - Shotgun with spread fire mechanics
  - Customizable weapon slots per ship
- **Physics-Based Movement**: Realistic momentum and acceleration mechanics
- **Health & Ammo Management**: Strategic resource management with reload mechanics

### Game Modes
- **Level Mode**: Complete structured levels with increasing difficulty
- **Endless Mode**: Survive as long as possible (coming soon)

### Progression System
- **Coin Rewards**: Earn coins by completing levels
- **Ship Hangar**: Manage and switch between unlocked ships
- **Upgrade System**: Framework for ship and weapon upgrades (in development)

## 🛠️ Technical Architecture

### Design Patterns
The game uses **Builder Pattern** extensively for creating game objects:
- `PlayableShipBuilder` & `PlayableShipBuilderDirector` for player ships
- `BaseEnemyBuilder` & `BaseEnemyBuilderDirector` for enemies
- `GunBuilder` & `GunBuilderDirector` for weapons
- `BulletBuilder` & `BulletBuilderDirector` for projectiles

### Project Structure
```
space_shooter/
├── main.py                 # Entry point and game loop
├── mycode/                 # Core game modules
│   ├── ships.py           # Player ship classes and builders
│   ├── enemies.py         # Enemy classes and builders
│   ├── weapons.py         # Weapon system (guns, bullets)
│   ├── bullets.py         # Bullet mechanics
│   ├── levels.py          # Level and wave management
│   ├── UI.py              # UI components and menus
│   ├── player.py          # Player data management
│   ├── hp.py              # Health bar system
│   ├── physics.py         # Physics engine
│   ├── clips.py           # Ammo and reload mechanics
│   ├── spawners.py        # Enemy spawn patterns
│   └── utils.py           # Utility functions
├── gameData/              # JSON configuration files
│   ├── playerShips.json   # Ship definitions
│   ├── enemies.json       # Enemy configurations
│   ├── guns.json          # Weapon specifications
│   ├── bullets.json       # Bullet properties
│   └── levels.json        # Level wave definitions
├── images/                # Game sprites and UI assets
├── sounds/                # Sound effects
└── enemies/               # Enemy sprite images
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Pygame library

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd space_shooter-master
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Controls
- **W/A/S/D**: Move ship (up/left/down/right)
- **Left Shift**: Boost/drift mode (reduced friction)
- **Numpad 0**: Fire weapons
- **P or ESC**: Pause game
- **Mouse**: Navigate menus and select options

### Game Flow
1. Start from the main menu
2. Select "Levels" to begin campaign mode
3. Choose a level from the level selection screen
4. Survive enemy waves and complete objectives
5. Earn coins and unlock new ships

### Tips
- Manage your ammo carefully - weapons need to reload
- Use drift mode (Shift) for precise dodging
- Different ships have different weapon configurations
- Health doesn't regenerate between waves

## 📊 Game Configuration

All game data is stored in JSON files for easy modding:

### Ship Configuration (`playerShips.json`)
```json
{
  "name": "Ship1",
  "mass": 300,
  "force": 1500,
  "hp_amount": 200,
  "path": "./images/SpaceShips/Ship_1.png",
  "scale": 2.0,
  "slots": [...]
}
```

### Weapon Configuration (`guns.json`)
```json
{
  "name": "Kinetic",
  "bullet_name": "KineticBullet",
  "force": 3500,
  "interval": 0.1,
  "clip": {
    "max_ammo": 50,
    "reload_time": 3.0
  }
}
```

### Level Design (`levels.json`)
Define custom waves with spawn patterns:
- `single`: Spawn one enemy
- `pair`: Spawn two enemies
- `line`: Spawn enemies in a line formation

## 🔧 Development

### Key Classes

**Player Ship System**
- `PlayableShip`: Main player ship class with movement and combat
- `PlayableShipBuilder`: Constructs ships with specific configurations
- `PlayableShipBuilderDirector`: Manages ship creation from JSON data

**Enemy System**
- `BaseEnemy`: Base enemy class with AI and combat
- `BaseEnemyBuilder`: Constructs enemies
- `BaseEnemyBuilderDirector`: Manages enemy creation

**Level Management**
- `WaveManager`: Handles wave spawning from level data
- `LevelManager`: Coordinates level progression and timing

**UI Components**
- `Button`: Generic button with hover effects
- `LevelButton`: Specialized button for level selection
- `ImageButtonDisplayer` & `TextButtonDisplayer`: Button rendering strategies

### Adding New Content

**Add a New Ship:**
1. Add ship sprite to `images/SpaceShips/`
2. Define ship in `gameData/playerShips.json`
3. Configure weapon slots and stats

**Add a New Weapon:**
1. Define bullet in `gameData/bullets.json`
2. Define gun in `gameData/guns.json`
3. Add sound effects to `sounds/shot_sounds/`

**Create a New Level:**
1. Edit `gameData/levels.json`
2. Define waves with spawn patterns
3. Set coin rewards

## 🐛 Known Issues & Future Features

### In Development
- Endless mode implementation
- Shop system for upgrades
- Ship upgrade mechanics
- Additional weapon types (flamethrower, laser)
- More enemy types and behaviors

### Planned Features
- Particle effects system
- Boss battles
- Power-ups and collectibles
- Leaderboard system
- Sound and music integration

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Create custom levels and ships

## 🎨 Credits

- Game developed using Python and Pygame
- Sprite assets from various sources
- Sound effects from open source libraries

---

**Enjoy defending the planet! 🌍✨**
