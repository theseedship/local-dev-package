# 🏃 Démarrage Rapide - 5 minutes chrono !

Ce guide ultra-rapide pour les développeurs pressés qui veulent démarrer immédiatement.

## 🎯 En 3 commandes

```bash
# 1. Cloner et entrer dans le projet
git clone https://github.com/theseedship/local-dev-package.git && cd local-dev-package

# 2. Copier les configs
cp .env.example .env && cp .env.local.example .env.local

# 3. Démarrer !
python start_services.py
```

## 📊 Tableau de bord des services

Une fois démarré, vos services sont accessibles :

```
🌐 Supabase    → http://localhost:8000    (BDD + Auth + Storage)
🤖 n8n         → http://localhost:5678    (Automatisation)
📦 Minio       → http://localhost:9001    (Stockage S3)
🐰 RabbitMQ    → http://localhost:15672   (Messages)
🧠 Open WebUI  → http://localhost:3000    (IA)
```

## 🔌 Connexion depuis votre app

### JavaScript/TypeScript
```javascript
// Base de données
const SUPABASE_URL = 'http://localhost:8000'
const SUPABASE_KEY = 'eyJhbGc...' // Depuis .env

// Stockage S3
const S3_ENDPOINT = 'http://localhost:9000'
const S3_BUCKET = 'test-minio'

// RabbitMQ
const AMQP_URL = 'amqp://guest:guest@localhost:5672'
```

### Variables d'environnement
```env
# Dans votre projet
DATABASE_URL=postgresql://postgres:your-password@localhost:5432/postgres
S3_ENDPOINT=http://localhost:9000
RABBITMQ_URL=amqp://guest:guest@localhost:5672
```

## 🛑 Commandes essentielles

```bash
# Voir l'état
./dc.sh ps

# Logs d'un service
./dc.sh logs -f postgres

# Arrêter
./dc.sh down

# Redémarrer un service
./dc.sh restart supabase-studio
```

## 💡 Tips Pro

1. **Performance** : Utilisez `--profile cpu` si vous avez un GPU
2. **Mémoire** : Démarrez seulement les services nécessaires
3. **Debugging** : Les logs sont votre ami → `./dc.sh logs -f`

C'est parti ! 🚀