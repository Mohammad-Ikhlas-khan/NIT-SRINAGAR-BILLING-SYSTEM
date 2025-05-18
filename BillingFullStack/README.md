# NIT Srinagar Billing System

## Run using Docker

- Make sure Docker is installed and running

### Clone the repository

#### HTTPS

```bash
git clone https://github.com/UsaidAijaz/BillingFullStack.git
```

#### SSH

```bash
git clone git@github.com:UsaidAijaz/BillingFullStack.git
```

### Change directory to project folder
```bash
cd BillingFullStack
```

### Create Environment Variables File
- See `.env_base` file and create your own `.env` file
- You may directly copy-paste the `.env_base` to `.env`

### Build the app
```bash
docker compose -p billing-app build
```

### Start the app
```bash
docker compose -p billing-app up -d
```

### Stop the app
```bash
docker compose -p billing-app down
```

## Run without Docker

### Setup the app

#### Clone the repository

##### HTTPS

```bash
git clone https://github.com/UsaidAijaz/BillingFullStack.git
```

##### SSH

```bash
git clone git@github.com:UsaidAijaz/BillingFullStack.git
```

#### Change directory to project folder
```bash
cd BillingFullStack
```

#### Create a virtual environment

```bash
python3 -m venv venv
```

#### Activate the virtual environment

##### Unix

```bash
source venv/bin/activate
```

##### Windows

```bash
venv\Scripts\activate.bat
```

#### Install requirements

```bash
pip install -r requirements.txt
```

### Create Environment Variables File
- See `.env_base` file and create your own `.env` file
- You may directly copy-paste the `.env_base` to `.env`

#### Initialize the app

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py custom_csu --username 'admin' --password 'admin@123'
python3 manage.py app_init --username 'admin'
```

### Deactivate the virtual environment

```bash
deactivate
```

### Run the app

#### Activate the virtual environment

##### Unix

```bash
source venv/bin/activate
```

##### Windows

```bash
venv\Scripts\activate.bat
```

### Start the application

```bash
python3 manage.py runserver
```

### Deactivate the virtual environment

```bash
deactivate
```
