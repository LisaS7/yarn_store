# Table of Contents

1. [Brief](#brief)
2. [Rules](#rules)
3. [Technologies Used](#technologies-used)
4. [Running Instructions](#running-instructions)
   <br>
   <br>

# Brief

### Shop Inventory

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP

- The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
- The inventory should track manufacturers, including a name and any other appropriate details.
- The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  - This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
- Show an inventory page, listing all the details for all the products in stock in a single view.
- As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### Inspired by

eBay, Amazon (back end only), Magento

#### Possible Extensions

- Calculate the markup on items in the store, and display it in the inventory
- Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
- Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
- Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

&nbsp;

# Rules

It must NOT use:

- Any Object Relational Mapper (e.g. ActiveRecord)
- JavaScript. At all. Don't even think about it.
- Any pre-built CSS libraries, such as Bootstrap.
- Authentication. Assume that the user already has secure access to the app.

# Technologies Used

- HTML / CSS
- Python
- Flask
- PostgreSQL and the psycopg

# Running Instructions

1. Clone git repository
2. Create and activate a virtual environment inside the cloned repository

```
  cd yarn_store
  python3 -m venv venv
  source venv/bin/activate
```

3. Install from requirements.txt

```
pip install -r requirements.txt
```

4. Run the app with flask

```
flask run
```

# Screenshots

View details for all yarns.
![All Yarns View](screenshots/all_yarns.png?raw=true "All Yarns")

View colours, including stock level warning indicators. Order more stock.
![All Yarns View](screenshots/all_yarns.png?raw=true "All Yarns")
