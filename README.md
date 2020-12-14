# Backend for EzAccommodation

This is backend providing API that can process user register, login, creating post and so on...

## Installation

We assume that you have Python and Pip in your machine. If not then go install them first.
This installation is for Window, other platform may have slightly different syntax.

First you need to create a virtual machine

```bash
source> cd backend
source/backend> py -m venv venv
source/backend> cd venv/Scripts
source/backend/venv/Scripts> activate
```

Then you install django and other modules
Remember to activate virtual machine

```bash
(venv)source/backend> pip install -r requirements.txt
```

## Migrate the database

Remember to activate virtual machine

```bash
(venv)source/backend> py manage.py makemigations
(venv)source/backend> py manage.py migrate
```

## Get the Server running (at port 8000)

Remember to activate virtual machine

```bash
(venv)source/backend> py manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
