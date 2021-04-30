# An E-Commerce Platform following MVC Structure which can give services to people for buying things that for sale. #  
## Programming language use to build Backend of this website is Python. However, I have used python framework Django which help to build this website in a short time. ## 

Structure
---------------

Structure of the project files is doen by following MVC Structure. Which includes 3 Components: 
  1. Model  
    - Models.py file from the project files.  
    - It refers to the Data Related Logic.  
    - Interaction with database.  
    - It communicates with the controllers.  

  2. View  
    - All the Html, CSS file.  
    - What the end users see (UI).  
    - Communicates with the controller.  
    - While coding are passed as dynamic values from the controller.  

  3. Controller  
    - Views.py file from the project files.  
    - Handles all the user inputs through url.  
    - The interaction to an application starts here by the user interactions – mouse click, key press etc.  
    - Communicates with both Model and View.  
    - Contains all server side logic.  

Features
---------------

Features of the website(User):
  * Users can Signup using only with their email, username, password.  
  * Login can be done if the user have an existing account.  
  * Customers View all products in their homepage.  
  * They can also specifically see the description of a product.  
  * After deciding which product to buy, users can add the selected products in their cart.  
  * When there is one or more than one products in the cart, users can still continue their shopping and add products to the cart.  
  * Available products in the cart can be increased or decreased whenever a user want to do so.  

Featurees of the website(Admin):
  * Admin can add superuser.
  * A person that have superuser credential can access the admin panel.
  * In the admin panel, admin can add, edit and delete the products.
