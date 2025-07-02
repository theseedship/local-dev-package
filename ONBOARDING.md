# 🚀 Guide de Démarrage - Environnement de Développement Local

Ce guide vous accompagne pas à pas pour installer et utiliser votre environnement de développement local avec tous les services nécessaires.

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Démarrage rapide](#démarrage-rapide)
5. [Utilisation des services](#utilisation-des-services)
6. [Configuration personnalisée](#configuration-personnalisée)
7. [Résolution de problèmes](#résolution-de-problèmes)
8. [Pour aller plus loin](#pour-aller-plus-loin)

## 🎯 Vue d'ensemble

### Qu'est-ce que c'est ?

Un environnement de développement complet qui regroupe tous les outils dont vous avez besoin pour développer en local :

- **Base de données** (PostgreSQL)
- **Stockage de fichiers** (Minio/S3)
- **Messagerie** (RabbitMQ)
- **Backend complet** (Supabase)
- **Intelligence Artificielle** (Ollama, Flowise)
- **Automatisation** (n8n)
- **Et plus encore...**

### Pourquoi l'utiliser ?

✅ **Tout-en-un** : Plus besoin d'installer chaque service individuellement  
✅ **Isolé** : N'interfère pas avec votre système  
✅ **Reproductible** : Même environnement pour toute l'équipe  
✅ **Simple** : Quelques commandes suffisent  

## 💻 Prérequis

### Matériel requis

- **Ordinateur** : Windows, Mac ou Linux
- **RAM** : Minimum 8 GB (16 GB recommandé)
- **Espace disque** : Au moins 20 GB disponibles

### Logiciels à installer

1. **Docker Desktop** 
   - 🪟 [Windows](https://docs.docker.com/desktop/install/windows-install/)
   - 🍎 [Mac](https://docs.docker.com/desktop/install/mac-install/)
   - 🐧 [Linux](https://docs.docker.com/desktop/install/linux-install/)

2. **Git**
   - [Télécharger Git](https://git-scm.com/downloads)

3. **Python** (version 3.8 ou plus)
   - [Télécharger Python](https://www.python.org/downloads/)

4. **Un éditeur de code** (recommandé)
   - [VS Code](https://code.visualstudio.com/)
   - [Cursor](https://cursor.sh/)

## 📦 Installation

### 1. Cloner le projet

Ouvrez un terminal et exécutez :

```bash
# Créer un dossier pour vos projets
mkdir -p ~/workspace
cd ~/workspace

# Cloner le projet
git clone https://github.com/theseedship/local-dev-package.git
cd local-dev-package
```

### 2. Configuration initiale

```bash
# Copier le fichier de configuration exemple
cp .env.example .env

# Créer votre configuration personnelle
cp .env.local.example .env.local
```

### 3. Éditer vos configurations

Ouvrez `.env.local` dans votre éditeur et personnalisez si nécessaire :

```env
# Exemple de configuration personnalisée
S3_BUCKET=mon-bucket-local
POSTGRES_PASSWORD=mon-mot-de-passe-securise
```

> 💡 **Astuce** : Les valeurs par défaut fonctionnent très bien pour commencer !

## 🚀 Démarrage rapide

### Méthode 1 : Script automatique (Recommandé)

```bash
# Démarrer tous les services essentiels
python start_services.py

# Ou démarrer des services spécifiques
python start_services.py --services postgres,supabase,minio
```

### Méthode 2 : Docker Compose

```bash
# Utiliser le script wrapper qui charge automatiquement vos configs
./dc.sh up -d

# Voir les logs
./dc.sh logs -f
```

### Vérifier que tout fonctionne

```bash
# Voir l'état des services
./dc.sh ps

# Ou avec Docker directement
docker ps
```

## 🛠 Utilisation des services

### Accès aux interfaces web

Une fois les services démarrés, vous pouvez accéder aux interfaces :

| Service | URL | Description |
|---------|-----|-------------|
| **Supabase Studio** | http://localhost:8000 | Interface d'administration base de données |
| **n8n** | http://localhost:5678 | Automatisation et workflows |
| **Minio Console** | http://localhost:9001 | Gestion du stockage S3 |
| **RabbitMQ** | http://localhost:15672 | Interface de gestion des messages |
| **Open WebUI** | http://localhost:3000 | Interface pour l'IA locale |

### Identifiants par défaut

| Service | Utilisateur | Mot de passe |
|---------|-------------|--------------|
| Supabase | `supabase` | `this_password_is_insecure_and_should_be_updated` |
| Minio | `minioadmin` | `minioadmin` |
| RabbitMQ | `guest` | `guest` |

> ⚠️ **Important** : Changez ces mots de passe dans `.env.local` pour la production !

## ⚙️ Configuration personnalisée

### Structure des fichiers de configuration

```
local-dev-package/
├── .env              # Configuration de base (ne pas modifier)
├── .env.local        # VOS configurations personnelles
├── docker-compose.yml # Services disponibles
└── dc.sh            # Script helper
```

### Ajouter vos propres variables

Dans `.env.local` :

```env
# Mes configurations personnelles
MON_API_KEY=ma-cle-secrete
MON_SERVICE_URL=http://mon-service:3000
```

### Activer/Désactiver des services

Dans `start_services.py`, modifiez les profils :

```python
# Exemple : Ajouter RabbitMQ au profil de base
python start_services.py --profile base --services rabbitmq
```

## 🔧 Résolution de problèmes

### Problèmes courants

#### 1. "Cannot connect to Docker daemon"

**Solution** : Assurez-vous que Docker Desktop est lancé

```bash
# Vérifier que Docker fonctionne
docker version
```

#### 2. "Port already in use"

**Solution** : Un service utilise déjà le port

```bash
# Voir quel processus utilise le port (exemple pour le port 5432)
# Sur Mac/Linux
lsof -i :5432

# Sur Windows
netstat -ano | findstr :5432
```

#### 3. Services qui ne démarrent pas

**Solution** : Vérifier les logs

```bash
# Voir les logs d'un service spécifique
./dc.sh logs postgres
./dc.sh logs supabase-studio
```

### Commandes utiles

```bash
# Redémarrer un service
./dc.sh restart nom-du-service

# Arrêter tous les services
./dc.sh down

# Nettoyer complètement (attention aux données !)
./dc.sh down -v

# Reconstruire les images
./dc.sh build --no-cache
```

## 📚 Pour aller plus loin

### Intégrer votre projet

1. **Créer votre projet** dans un dossier séparé :
```bash
cd ~/workspace
npx create-solid-app@latest mon-projet
cd mon-projet
```

2. **Configurer les connexions** aux services :
```javascript
// Exemple de connexion à Supabase
const supabaseUrl = 'http://localhost:8000'
const supabaseKey = process.env.SUPABASE_ANON_KEY
```

### Récupérer les mises à jour

```bash
# Récupérer les dernières améliorations
git pull upstream main

# Voir les changements
git log --oneline -5
```

### Contribuer au projet

1. Créez une branche pour vos modifications
2. Faites vos changements
3. Testez localement
4. Créez une Pull Request

## 🆘 Besoin d'aide ?

- **Documentation technique** : Consultez le [README.md](README.md)
- **Problème spécifique** : Créez une [issue sur GitHub](https://github.com/theseedship/local-dev-package/issues)
- **Questions** : Contactez l'équipe de développement

---

## 🎉 Félicitations !

Vous êtes maintenant prêt à développer avec votre environnement local complet ! 

### Prochaines étapes suggérées :

1. ✅ Explorer les interfaces web des services
2. ✅ Tester la connexion depuis votre application
3. ✅ Personnaliser votre `.env.local`
4. ✅ Commencer à développer !

Bon développement ! 🚀