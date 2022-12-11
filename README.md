# *Loan Qualifier Application*

The purpose of the loan qualifier application is to allow a user to swiftly and efficiently figure out if they qualify for a loan from a list of banks. They are prompted to enter user data and the function will determine whether or not any banks match their criteria.

![An image for the header of the Repository](desktop/rc_unsecuredpl_hero.png)

---

## **Required Technologies**

In order to run the application, you first must install two Python libraries; fire and questionary.

'fire' (0.3.1)
'questionary' (1.5.2)

---

## Installation Guide

You can install both the fire and questionary libraries to your device by running the following prompt in your command line interface (CLI).

'''pip install fire'''
'''pip install questionary'''

---

## Usage

You can initiate the application in your CLI by entering 'python app.py'. The code will run by asking the user to input the location of the CSV file containing the list of banks that the application will filter through *(NOTE: The entry must be in the format "./<'folder'>/<'filename'>.csv")*

The user will be prompted to enter their data that the application will use to filter through the list of banks. It asks for the user's credit score, monthly debt, monthly income, desired loan amount, and home value. 

'''python
 credit_score = questionary.text("What's your credit score?").ask()
 debt = questionary.text("What's your current amount of monthly debt?").ask()
 income = questionary.text("What's your total monthly income?").ask()
 loan_amount = questionary.text("What's your desired loan amount?").ask()
 home_value = questionary.text("What's your home value?").ask()
'''

Following this, if there are any loans that meet their criteria, it will inform the user and ask if they would like to download the list of qualifying loans to their device as a CSV file. If 'yes', they will be prompted to enter the location on their device where they want the file to be downloaded. *(NOTE: If there are no qualifying loans or they choose not to download the list as a CSV, the application will exit.)*

'''python
 if len(qualifying_loans)>= 1:
        save_file = questionary.confirm('Would you like to save the list of qualifying loans as a CSV file?').ask()
        if save_file:
            file_location = questionary.text('Input the location where you would like the file to be saved.').ask()
            csvpath = Path(file_location)
            print(f'Saving list of qualifying loans to...{csvpath}')
            with open(csvpath, 'w', newline= '') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(header)
                for row in qualifying_loans:
                    csvwriter.writerow(row)
        else:
            sys.exit('Thank you for using the loan qualifier application.')
    else:
        sys.exit('There are 0 loans that meet your criteria.')
'''
 
The code will appear in the CLI as follows:

![Image of the CLI output](desktop/screenshot.png)

---

## Contributors

Adam Jimenez - FinTech Student

---

## License

2022 edX Bootcamps
