from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account'] # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # Call balance function to render that account's Balance Sheet
    content = {'form': form} # Pass content to the template in a dictionary
    return render(request, 'checkbook/index.html', content)

def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve Account Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # Check to see if the submitted form is valid and if so saves the form
            form.save() # Saves new account
            return redirect('index') # Returns user back to the home page
    content = {'form': form} # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # Retrieve the requested account using its PK
    transactions = Transaction.Transactions.filter(account=pk) # Retrieve all of that account's transactions
    current_total = account.initial_deposit # Create account total variable, starting with initial deposit value
    table_contents = {} # Create a dictionary into which transaction information will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount # If deposit then add amount to balance
            table_contents.update({t: current_total}) # Add transaction and total to the dictionary
        else:
            current_total -= t.amount # Else its withdrawal so subtract amount from balance
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account'] # Retrieve which account the transaction was for
            form.save()
            return balance(request, pk) # Renders balance of the account's Balance Sheet
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
