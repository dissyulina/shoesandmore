# **Shoes And More - Testing**  

[Back to the main README.md file](https://github.com/dissyulina/shoesandmore#shoes-and-more)  

[Back to the Testing section in main README.md file](https://github.com/dissyulina/shoesandmore#testing)

[View the live website here](https://shoes-and-more.herokuapp.com/)  

## **Table of Contents**  
1. User Stories Testing  
   - Unregistered Users' Goals  
   - Registered Users' Goals  
   - Administrative Account Holder's Goals  
2. Autoprefixer CSS  
3. Manual Testing  
   - Browsers Compatibility  
   - Devices  
   - Responsiveness  
   - Links  
   - Forms  
   - Defensive Testing  
4. W3C Validator Testing  
   - HTML  
   - CSS  
5. JSHint Testing  
6. Pep8 Online Testing  
7. Lighthouse Testing  

<br/>

The website was extensively tested during the development and after development by using:
- ```console.log()``` and developer tools for front-end  
- Printing variables to the terminal for back-end  
- Manual testing and developing based on the user stories  
- Automated testing on Django at the end of development phase. 
- Few other testing using programs 

The testings are documented below.


### **1. User Stories Testing**  
As a shopper I want to be able to:

1. *Quickly identify what products/services the site sells.*   
   Company logo is visible right at the top-center of the homepage. The company name is straightforward describing what products we sell. On top of that, the hero image is clearly picturing shoes as the main product. As users scrolls down the home page, they will find various navigation using large images of the products.     
   ![Landing Page](readme-testing-files/testing/user-stories/home-1.png "Landing Page")  

2. *Quickly identify deals and special offers.*  
   As users scrolls down the homepage, they will find the Final Sale section. When the 'Shop Now' button is clicked, they will be directed to the products page with all the sale items already filtered.   
   ![Sale Banner](readme-testing-files/testing/user-stories/sale.png "Sale Banner")   

3. *Search for a product.*  
   Users can search for a product right away when they open the website. The search functionality is located at the top-left of screen on desktop, and on right side on mobile. 
   ![Search for Product](readme-testing-files/testing/user-stories/navbar-search.png "Search for Product")  

4. *Identify a glimpse of most populars products.*  
   Still on the homepage, users will also find 8 most popular (best-sellers) products on the website. They are displayed as a multi-items carousel, and users can navigate to the left and right by clicking the arrows.  
   ![Best Sellers Products](readme-testing-files/testing/user-stories/best-sellers.png "Best Sellers Products")  

5. *View all products, and easily navigate between categories.*  
   There are 3 main categories in this website - Women, Men, and Kids. When users click on a category, it will display all subcategories within it - Boots, Sneakers, Flats, etc. For desktop, there's a side navigation which will make a great user experience to navigate between the categories and subcategories. On mobile, the side nav is replaced by a dropdown option. Breadcrumb Navigation is available as well to allow users to navigate back to the more general category.  
   ![Navigation - desktop](readme-testing-files/testing/user-stories/navigation.png "Navigation - desktop")   
   ![Navigation - mobile](readme-testing-files/testing/user-stories/navigation-mobile.png "Navigation - mobile")  

6. *Sort by price, by rating, and by popularity.*    
   The sort functionality is positioned on the top-left on the products page.  
   ![Sort functionality](readme-testing-files/testing/user-stories/sort.png "Sort functionality")   

7. *View individual product's page and read the relevant information.*  
   Users can click on the product's image and it will direct them to the Individual Product page where they can find all the relevant information.  
   ![Product's information](readme-testing-files/testing/user-stories/product-info.png "Product's information")   

8. *Read a product's review.*   
   On the Individual Product page, users can scroll down and find the review below the product's information.  
   ![Product's reviews](readme-testing-files/testing/user-stories/reviews.png "Product's reviews")   

9. *Easily select size and quantity of the product, and add it to shopping bag.*   
   Users can easily select the size and quantity, and then click on Add To Bag button to buy it.   
   ![Select Size and Quantity](readme-testing-files/testing/user-stories/select-size.png "Select Size and Quantity")  

10. *View the shopping bag with products added in it.*   
   If users add a product to the shopping bag, a toast will show up at the top-right corner to inform the user about the shopping bag.  
   ![Shopping Bag Toast](readme-testing-files/readme/toast-success.png "Shopping Bag Toast")  
   Users can also view the Shopping Bag page by clicking the navigation in the Navigation Bar, or by clicking the 'Go To The Shopping Bag' button inside the toast.  
   ![Shopping Bag Page](readme-testing-files/testing/user-stories/bag.png "Shopping Bag Page")  

11. *Update the shopping bag by adjusting the quantity of the products, or removing them from the shopping bag.*   
   Users can easily update or adjust the quantity of the product by selecting the quantity, and the Subtotal will be updated accordingly. If users want to remove the product from the shopping bag, they can click on the Trash icon.  
   ![Adjust Bag](readme-testing-files/testing/user-stories/bag-adjust.png "Adjust Bag")  

12. *Checkout and easily enter my payment information.*  
13. *Feel my personal and payment information is safe and secure.*  
   By clicking the 'Secure Checkout' button on the Shopping Bag page, users will be directed to the Checkout page. In the payment section, the card payment input is divided into the number, expired date, cvc, and zip code.   
   ![Checkout form](readme-testing-files/testing/user-stories/checkout-information.png "Checkout form")  

14. *View an order confirmation after purchasing.*  
   After users fill out the checkout form and click on the 'Complete Order' button, they will be directed to a success page where users can see their order information. At the same time they will also get an email order confirmation on their inbox.  
   ![Order confirmation](readme-testing-files/testing/user-stories/order-confirmation.png "Order confirmation")  

15. *Receive an email confirmation after purchasing.*  
   As mentioned above, users will also get an email confirmation to their inbox everytime they complete an order.   
   ![Email confirmation](readme-testing-files/testing/user-stories/email.png "Email confirmation")  

16. *Read relevant articles/ blogs about shoes or accessories.*   
   Users can find the Articles page by clicking the link to the articles on footer, or on the homepage. Users can choose to view an article by clicking one of them.  
   ![All articles](readme-testing-files/testing/user-stories/articles.png "All articles")  
   ![Individual article](readme-testing-files/testing/user-stories/individual-article.png "Individual article")  

17. *Easily navigate within the site, through Navigation Bar and Footer.*
   Navigation Bar and Footer are available on all pages. Navigation bar is fixed on the top of screen, so it will stays on the screen as the users scroll down to provide easy access to navigate throughout the site.   
   Navbar and Footer on desktop:   
   ![Navbar on desktop](readme-testing-files/readme/navbar-desktop.png "Navbar on desktop")   
   ![Footer on desktop](readme-testing-files/readme/footer-desktop.png "Footer on desktop")   
   Navbar and Footer on mobile:   
   ![Navbar on mobile](readme-testing-files/testing/user-stories/navbar-mobile.png "Navbar on mobile")  
   ![Footer on mobile](readme-testing-files/testing/user-stories/footer-mobile.png "Footer on mobile")     

18. *Easily register for an account.*   
   By clicking the 'Sign In' link on the left side of the Navbar on desktop, or clicking the user icon on mobile, users can either register or login to the website. Users then will be directed to the Register / Sign Up page or Log In page.  
   ![Register](readme-testing-files/testing/user-stories/register.png "Register") ![Log In](readme-testing-files/testing/user-stories/login.png "Log In")   

19. *Find FAQ section for my questions.*   
   Users can find the link to go to the FAQ page in the footer.  
   ![FAQ](readme-testing-files/testing/user-stories/faq.png "FAQ")   

20. *Contact the shop via a contact form.*   
   Users can also find the link to go to contact page in the footer.   
   ![Contact form](readme-testing-files/testing/user-stories/contact-form.png "Contact form")   

<br/>

As a registered user/ shopper, I want to be able to:
1. *Access all functionalities that an unregistered shopper can do.*   
   All of the features and functionality above are certainly also available and accessible for registered / logged-in users.   

2. *Easily login or logout.*  
   Logged-in users can log out by clicking the user icon on the left side of the Navbar.  
   ![Logout link](readme-testing-files/testing/user-stories/logout-link.png "Logout link")      

3. *Easily recover my password in case I forget it.*   
   On the Log In page, there's an option to change your password below the buttons. When clicked, it will lead the users to the password reset page.   
   ![Password reset](readme-testing-files/testing/user-stories/password-reset.png "Password reset")      

4. *Receive an email confirmation after registering.*  
   After successfully register to the website, users then will be informed to check on their inbox.  
   ![Email verification 1](readme-testing-files/testing/user-stories/email-verify-1.png "Email verification 1")      
   In the user's inbox, an email from Shoes And More is found. Users then will be asked to verify their email by clicking the link provided.  
   ![Email verification 2](readme-testing-files/testing/user-stories/email-verify-2.png "Email verification 2")      
   After the link is clicked, users then will be directed back to the website, and to confirm the email address.   
   ![Email verification 3](readme-testing-files/testing/user-stories/email-verify-3.png "Email verification 3")      

5. *Have a personalized user profile where I can see my order history and change my information.*   
   By navigating to the My Account in the Navbar (or user icon on mobile), and click on My Profile, users can see their profile page. This page is divided into 3 pills/tabs - My Information, My Purchases, and Ratings/Reviews. User can see/update their delivery information and see their order history by clicking My Information pill and My Purchases pill respectively.  
   ![Update information](readme-testing-files/testing/user-stories/profile-information.png "Update information")  
   ![Order history](readme-testing-files/testing/user-stories/profile-orderhistory.png "Order history")   

6. *Review products that I have purchased before.*  
   User can review the products that they have already purchased before by navigating to the Ratings/Reviews pill on the My Profile page. 
   ![Products to be reviewed](readme-testing-files/testing/user-stories/profile-reviews.png "Products to be reviewed")   
   By clicking the Give Review button, users will be directed to the Add Review page.  
   ![Add review](readme-testing-files/testing/user-stories/add-review.png "Add review")  

7. *Edit and delete my reviews.*  
   Once users submit a review, they can view the review by navigating to the Individual Product page in the Reviews section. If the user owns the review, there will be two buttons available under the review - Edit button and Delete button.  
   ![Review](readme-testing-files/testing/user-stories/review.png "Review")  

   When the Edit button is clicked, the user will be directed to the Edit Review page, which has a similar layout with the Add Review page. The only difference is, on Edit Review, the input rating and review are already pre-populated with the existing review. User can submit the updated review by clicking the 'Submit Review' button.   
   ![Edit review](readme-testing-files/testing/user-stories/edit-review.png "Edit review")   

   When the Delete button is clicked, a modal will show up to confirm users if they really want to delete their review. To confirm, click the 'Yes, Delete' button.  
   ![Modal to delete review](readme-testing-files/testing/user-stories/modal-delete-review.png "Modal to delete review")  

8. *Add products to the wishlist, so I can quickly find products I'd like to purchase.*  
   Users can add products to their favorites by clicking the heart icon on the top-right of each product. This heart icon then turned red if the product is in the user's favorites.  
   ![Heart icon to add to favorites](readme-testing-files/testing/user-stories/heart-icon.png "Heart icon to add to favorites")    

9. *Remove products from the wishlist, so I can remove products I don't wish to purchase.*  
10. *Easily put the wishlist products into the shopping bag.*   
   By clicking the Favorites link on the Navbar (heart icon on mobile's Navbar), user can navigate to the Favorites page to view all products the user has added to favorites. Users can remove products from the Favorites by clicking the Trash-can icon on the top-right of each product. Users can also directly add the product to the shopping bag by choosing a size and then click on 'Add to Bag' button.  
   ![Favorites](readme-testing-files/testing/user-stories/favorites.png "Favorites")    


As an admin and store management, I want to be able to:
1. *Add a product.*   
   Admin can add a product to the website by logging in as admin, navigate to My Account and choose Product Management. Admin then will be directed to the Add Products page. After filling out the form, they can click 'Add Product' button.   
   ![Add product](readme-testing-files/testing/user-stories/add-product.png "Add product")   

2. *Edit or update a product.*   
   Admin can edit a product by logging in as admin, navigate to the Products page or the Individual Product page and click on Edit link.  
   ![Edit and Delete product](readme-testing-files/testing/user-stories/admin-edit-delete.png "Edit and Delete product")   

   Admin then will be directed to the Edit Products page. After filling out the form, they can click 'Edit Product' button.  
   ![Edit product](readme-testing-files/testing/user-stories/edit-product.png "Edit product")   

3. *Delete a product.*   
   Admin can delete a product by logging in as admin, navigate to the Products page or the Individual Product page and click on Delete link. A modal will then show up to confirm the deletion. Admin can confirm it by clicking on the 'Yes, Delete' button.  
   ![Edit and Delete product](readme-testing-files/readme/delete-product-modal.png "Edit and Delete product")   

<br/>  

### **2. Auto Prefixer CSS**   
[Autoprefixer CSS](https://autoprefixer.github.io/) was used to add CSS vendor prefixes to the CSS rules after the developing process was done, to ensure that the they work across all browsers.  

<br/>  

### **3. Manual Testing by The Developer**  
#### **Browsers Compatibility**   
The website was tested through the following browsers: Google Chrome, Microsoft Edge, Opera, Mozilla Firefox, and Safari (iOS) browsers.  

#### **Devices**  
The website was also viewed on the following devices:  
- Windows Desktop  
- Windows Laptop  
- Tablets: iPad Mini 2 and iPad 2018  
- Mobile: iPhone7, iPhone 8, iPhone 12 Mini, Asus Zenfone Max Pro M2, and LG G5
- Friends and family members were asked to review the site on their devices and to point out any bugs and/or user experience issues.  

#### **Responsiveness**   
To check the responsiveness of the website across all devices, the developer tools are used regularly during the developing process. Based on the  
**Result**: 

#### **Links**   
The links were tested to ensure that:  
- All navigation links are linking correctly.  
- All buttons on the forms are working (to cancel or to submit the form).  
- The social media buttons are working and opening in a new tab.  

**Result**: All of the above are working properly.  

#### **Forms**  
The form was also tested to ensure that:  
- The required attributes are working.  
- The regex patterns for username and password are working.  
- There's a validation message that explains the correct format if the user filled in the wrong format (for username and password).  
- If a user fills out the wrong format, it won't break the website. For example, if I fill in letters in the "Servings" or "Prep + Cooking Time" field, it won't cause any error to the website.  