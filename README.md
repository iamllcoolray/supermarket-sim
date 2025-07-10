# Assignment 3: Interactive Supermarket Simulation with Data Mining

## Objective

In this homework assignment, you are required to design a website or application that serves as an interactive interface simulating a supermarket shopping experience. The goal is to combine user interaction with fundamental data mining techniques.

## Requirements

1.  Interactive Interface

    - Your interface must include at least 10 distinct items, such as milk, bread, basketball, etc.

    - Each item should be represented as a clickable button that allows the user to select products to create transactions.

2.  Transaction Creation and Storage

    - Users should be able to freely select items to form a transaction.
      Example: Transaction 1 = {milk, bread}

    - Your program must store all user transactions in an appropriate data structure or database.

    - Please note that in this assignment, how you store the data is one of the most critical aspects. You should carefully design your storage approach and may choose to maintain the data in multiple forms as needed to support different requirements.

3.  Minimum Number of Transactions

    - Users must create at least 5 transactions before they can proceed to data mining.

4.  Data Mining Analysis

    - After the minimum number of transactions is created, the user should be able to click
      a button to trigger your program to perform data mining analysis.

    - Your program must implement two types of data mining tasks:

      - Clustering (e.g., K-means clustering)
        Note: if only a small number of transactions are created (e.g., 5 to 10), the
        clustering results may lack statistical meaning and may not reveal clear or stable
        patterns. Therefore, you are encouraged to generate enough transactions (e.g., 30) to make the clustering output more meaningful and interpretable.

    - Association Rule Mining (e.g., Apriori algorithm) You may select specific algorithms from those covered in our course.

5.  Testing

    - You must test your program from the user’s perspective to ensure that all components, from the user interface to transaction storage and data mining, function correctly and logically.

    - Please ensure that executing your source code will directly produce a fully functional application that meets all specified requirements. By default, the instructor will not review your code line by line to verify its correctness, but will instead rely on testing your application’s functionality.

6.  Extra Features (Optional)

    - You are encouraged to add extra functions or improve the UI design according to your understanding.

    - Well-executed additional features can earn you up to 20 extra points.

## Deliverable

1.  A short report/README to explain your assignment. (PDF format)

2.  An executable source code.

3.  Put all files into one folder and compress this folder to submit.

## Setup

**Python Version 3.13+ (3.13.3 - used)**

Fork the Project and the download the repository.

### Create a Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```
python3 -m pip install -r requirements.txt
```

### Run the Project

```
python3 app.py
```

# Assignment 3: Interactive Supermarket Simulation with Data Mining

## Objective

In this homework assignment, you are required to design a website or application that serves
as an interactive interface simulating a supermarket shopping experience. The goal is to combine user interaction with fundamental data mining techniques.

## Requirements

1.  Interactive Interface

    - Your interface must include at least 10 distinct items, such as milk, bread, basketball, etc.

    - Each item should be represented as a clickable button that allows the user to select products to create transactions.

2.  Transaction Creation and Storage

    - Users should be able to freely select items to form a transaction.
      Example: Transaction 1 = {milk, bread}

    - Your program must store all user transactions in an appropriate data structure or database.

    - Please note that in this assignment, how you store the data is one of the most critical aspects. You should carefully design your storage approach and may choose to maintain the data in multiple forms as needed to support different requirements.

3.  Minimum Number of Transactions

    - Users must create at least 5 transactions before they can proceed to data mining.

4.  Data Mining Analysis

    - After the minimum number of transactions is created, the user should be able to click
      a button to trigger your program to perform data mining analysis.

    - Your program must implement two types of data mining tasks:

      - Clustering (e.g., K-means clustering)
        Note: if only a small number of transactions are created (e.g., 5 to 10), the
        clustering results may lack statistical meaning and may not reveal clear or stable
        patterns. Therefore, you are encouraged to generate enough transactions (e.g., 30) to make the clustering output more meaningful and interpretable.

    - Association Rule Mining (e.g., Apriori algorithm) You may select specific algorithms from those covered in our course.

5.  Testing

    - You must test your program from the user’s perspective to ensure that all components, from the user interface to transaction storage and data mining, function correctly and logically.

    - Please ensure that executing your source code will directly produce a fully functional application that meets all specified requirements. By default, the instructor will not review your code line by line to verify its correctness, but will instead rely on testing your application’s functionality.

6.  Extra Features (Optional)

    - You are encouraged to add extra functions or improve the UI design according to your understanding.

    - Well-executed additional features can earn you up to 20 extra points.

## Deliverable

1.  A short report/README to explain your assignment. (PDF format)

2.  An executable source code.

3.  Put all files into one folder and compress this folder to submit.

## Setup

**Python Version 3.13+ (3.13.3 - used)**

Fork the Project and the download the repository.

### Create a Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```
python3 -m pip install -r requirements.txt
```

### Run the Project

```
python3 app.py
```
