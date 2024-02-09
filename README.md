SETUP INSTRUCTIONS:
1. CD into backend directory. Should look like this in your terminal:
 ![image](https://github.com/MarcGugg/Cyber_Project/assets/109707298/90ca9449-04c4-4c1b-9386-3c5528dc6a62)
2. Install the following dependencies: FastAPI, SQLAlchemy, Alembic (for migrations), Faker (for seeders)
   - To install FastAPI, run this command:
       pip install "fastapi[all]"
       - for more info, reference the FastAPI documentaion/tutorial: https://fastapi.tiangolo.com/tutorial/
   - To install SQLAlchemy, run this command:
       pip install SQLAlchemy
       - the docs: https://docs.sqlalchemy.org/en/20/
   - To install Alembic: pip install alembic
       - the docs: https://alembic.sqlalchemy.org/en/latest/
   - To install faker: pip install Faker
       - the docs: https://faker.readthedocs.io/en/master/

3. Once all the dependencies are installed, in order to get the backend up and running, you will need to do the following:
  - Go into the backend/alembic/versions directory. there should be a .py file whose name is a random string of characters:
    ![image](https://github.com/MarcGugg/Cyber_Project/assets/109707298/b8ffff02-4916-458a-94dd-0c0673e04030)
  - There should be a variable called 'revision' that is assigned to a random string of characters:
    ![image](https://github.com/MarcGugg/Cyber_Project/assets/109707298/4fddcf03-315c-4239-a004-1d262844d7ee)
  - Back in the terminal, in the backend directory, run the following command: alembic upgrade *revision*, so in this case, alembic upgrade 5266bba21fc1
    - You may get an error of some kind, but it should only be a problem if the local database wasn't created, or if the database tables weren't created properly.
      To verify this, simply check the sql_app.db file, and cross reference the tables in that to the SQLAlchemy models/alembic migration file. If they match, the migrations worked.
      Otherwise, you may need to check the version of alembic you installed and/or check the docs/chatGPT

  - Once the migrations have been run, run the seeders with the following command: python seed.py
      - There should be absolutely no errors here. To verify that the seeders ran correctly, check all the tables in sql_app.py and make sure they all have data inside.


  - After all that, run the command: uvicorn sql_app.main:app --reload
      - This command is also found inside the file startup.txt in case you ever forget








4. CD into the frontend directory. Should look like this in your terminal:
   ![image](https://github.com/MarcGugg/Cyber_Project/assets/109707298/1e817eb4-e715-4b47-8a20-46cc6b3a597e)
5. For component styling (as sparse as it is), I use MaterialUI. To install, follow this guide: https://mui.com/material-ui/getting-started/installation/
6. By the end of the installations, your package.json should look like this:
   ![image](https://github.com/MarcGugg/Cyber_Project/assets/109707298/1e2d7a3f-0bb9-4553-bbcb-2be0ff053a72)

P.S If you have any issues with react, I use vite + react. to install, run this command: npm create vite@latest
 - tutorial: https://vitejs.dev/guide/

