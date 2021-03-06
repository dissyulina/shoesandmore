# **Shoes And More - Testing**  

[Back to the main README.md file](https://github.com/dissyulina/shoesandmore#shoes-and-more)  

[Back to the Testing section in main README.md file](https://github.com/dissyulina/shoesandmore#testing)

[View the live website here](https://shoes-and-more.herokuapp.com/)  

## **Table of Contents**  
1. [User Stories Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#1-user-stories-testing)  
   - [Shopper Goals](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#a-as-a-shopper-i-want-to-be-able-to)  
   - [Registered User & Shopper Goals](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#b-as-a-registered-user-shopper-i-want-to-be-able-to)  
   - [Administrative Account Holder's Goals](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#c-as-an-admin-and-store-management-i-want-to-be-able-to)  
2. [Autoprefixer CSS](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#2-auto-prefixer-css)  
3. [Manual Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#3-manual-testing-by-the-developer)  
   - [Browsers Compatibility](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#browsers-compatibility)  
   - [Devices](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#devices)  
   - [Responsiveness](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#responsiveness)  
   - [Links](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#links)  
   - [Forms](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#forms)  
4. [HTML & CSS Validator Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#html--css-validator-testing)  
   - [HTML](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#html)  
   - [CSS](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#css)  
5. [JavaScript Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#javascript-testing)  
6. [Flake8 and Pep8 Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#flake8-and-pep8-online-testing)  
7. [Lighthouse Testing](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#lighthouse-testing)  

<br/>

The website was extensively tested during the development and after development by using: 
- ```console.log()``` and developer tools for front-end.   
- Printing variables to the terminal for back-end.   
- Manual testing and development based on the user stories.   
- Automated testing on Django at the end of the development phase.  
- Few other testing using programs.   

The testings are documented below.  


## **1. User Stories Testing**  
### A. As a shopper I want to be able to:

1. *Quickly identify what products/services the site sells.*   
   The company logo is visible right at the top center of the homepage. The company name is straightforward describing what products we sell. On top of that, the hero image is picturing shoes as the main product. As users scroll down the home page, they will find various navigation using large images of the products.     
   ![Landing Page](readme-testing-files/testing/user-stories/home-1.png "Landing Page")  

2. *Quickly identify deals and special offers.*  
   As users scroll down the homepage, they will find the Final Sale section. When the 'Shop Now' button is clicked, they will be directed to the products page with all the sale items already filtered.   
   ![Sale Banner](readme-testing-files/testing/user-stories/sale.png "Sale Banner")   

3. *Search for a product.*   
   Users can search for a product right away when they open the website. The search functionality is located at the top-left of the screen on desktops, and on the right side on mobile.  
   ![Search for Product](readme-testing-files/testing/user-stories/navbar-search.png "Search for Product")  

4. *Identify a glimpse of the most popular products.*   
   On the homepage, users will also find the 8 most popular (best-sellers) products on the website. They are displayed in a multi-item carousel, and users can navigate to the left and right by clicking the arrows.  
   ![Best Sellers Products](readme-testing-files/testing/user-stories/best-sellers.png "Best Sellers Products")  

5. *View all products, and easily navigate between categories.*  
   There are 3 main categories on this website - Women, Men, and Kids. When users click on a category, it will display all subcategories within it - Boots, Sneakers, Flats, etc. For desktop, there's side navigation which will make a great user experience to navigate between the categories and subcategories. On mobile, the side nav is replaced by a dropdown option. Breadcrumb Navigation is available as well to allow users to navigate back to the more general category.  
   ![Navigation - desktop](readme-testing-files/testing/user-stories/navigation.png "Navigation - desktop")   
   ![Navigation - mobile](readme-testing-files/testing/user-stories/navigation-mobile.png "Navigation - mobile")  

6. *Sort by price, by rating, and by popularity.*    
   The sort functionality is positioned on the top left on the products page.  
   ![Sort functionality](readme-testing-files/testing/user-stories/sort.png "Sort functionality")   

7. *View the individual product's page and read the relevant information.*  
   Users can click on the product's image and it will direct them to the Individual Product page where they can find all the relevant information.  
   ![Product's information](readme-testing-files/testing/user-stories/product-info.png "Product's information")   

8. *Read a product's review.*   
   On the Individual Product page, users can scroll down and find the review below the product's information.  
   ![Product's reviews](readme-testing-files/testing/user-stories/reviews.png "Product's reviews")   

9. *Easily select the size and the quantity of the product, and add it to the shopping bag.*   
   Users can easily select the size and quantity and then click on Add To Bag button to buy it.   
   ![Select Size and Quantity](readme-testing-files/testing/user-stories/select-size.png "Select Size and Quantity")  

10. *View the shopping bag with products added to it.*   
   If users add a product to the shopping bag, a toast will show up at the top-right corner to inform the user about the shopping bag.  
   ![Shopping Bag Toast](readme-testing-files/readme/toast-success.png "Shopping Bag Toast")  
   Users can also view the Shopping Bag page by clicking the navigation in the Navigation Bar, or by clicking the 'Go To The Shopping Bag' button inside the toast.  
   ![Shopping Bag Page](readme-testing-files/testing/user-stories/bag.png "Shopping Bag Page")  

11. *Update the shopping bag by adjusting the quantity of the products, or removing them from the shopping bag.*   
   Users can easily update or adjust the quantity of the product by selecting the quantity, and the Subtotal will be updated accordingly. If users want to remove the product from the shopping bag, they can click on the Trash icon.  
   ![Adjust Bag](readme-testing-files/testing/user-stories/bag-adjust.png "Adjust Bag")  

12. *Checkout and easily enter my payment information.*  
13. *Feel my personal and payment information is safe and secure.*  
   By clicking the 'Secure Checkout' button on the Shopping Bag page, users will be directed to the Checkout page. In the payment section, the card payment input is divided into the number, expired date, CVC, and zip code.   
   ![Checkout form](readme-testing-files/testing/user-stories/checkout-information.png "Checkout form")  

14. *View an order confirmation after purchasing.*   
   After users fill out the checkout form and click on the 'Complete Order' button, they will be directed to a success page where users can see their order information. At the same time, they will also get an email order confirmation in their inbox.  
   ![Order confirmation](readme-testing-files/testing/user-stories/order-confirmation.png "Order confirmation")  

15. *Receive an email confirmation after purchase.*   
   As mentioned above, users will also get an email confirmation in their inbox every time they complete an order.   
   ![Email confirmation](readme-testing-files/testing/user-stories/email.png "Email confirmation")  

16. *Read relevant articles/ blogs about shoes or accessories.*     
   Users can find the Articles page by clicking the link to the articles on the footer, or on the homepage. Users can choose to view an article by clicking one of them.  
   ![All articles](readme-testing-files/testing/user-stories/articles.png "All articles")  
   ![Individual article](readme-testing-files/testing/user-stories/individual-article.png "Individual article")  

17. *Easily navigate within the site, through Navigation Bar and Footer.*   
   Navigation Bar and Footer are available on all pages. The navigation bar is fixed on the top of the screen, so it will stay on the screen as the users scroll down to provide easy access to navigate throughout the site.   
   Navbar and Footer on desktop:   
   ![Navbar on desktop](readme-testing-files/readme/navbar-desktop.png "Navbar on desktop")   
   ![Footer on desktop](readme-testing-files/readme/footer-desktop.png "Footer on desktop")   
   Navbar and Footer on mobile:   
   ![Navbar on mobile](readme-testing-files/testing/user-stories/navbar-mobile.png "Navbar on mobile")  
   ![Footer on mobile](readme-testing-files/testing/user-stories/footer-mobile.png "Footer on mobile")     

18. *Easily register for an account.*   
   By clicking the 'Sign In' link on the left side of the Navbar on desktop, or clicking the user icon on mobile, users can either register or login to the website. Users then will be directed to the Register / Sign Up page or Login page.  
   ![Register](readme-testing-files/testing/user-stories/register.png "Register") ![Log In](readme-testing-files/testing/user-stories/login.png "Log In")   

19. *Find the FAQ section for my questions.*    
   Users can find the link to go to the FAQ page in the footer.   
   ![FAQ](readme-testing-files/testing/user-stories/faq.png "FAQ")   

20. *Contact the shop via a contact form.*   
   Users can also find the link to go to contact page in the footer.   
   ![Contact form](readme-testing-files/testing/user-stories/contact-form.png "Contact form")   



[Back to top &uarr;](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#shoes-and-more---testing)  

<br/>

### B. As a registered user/ shopper, I want to be able to:
1. *Access all functionalities that an unregistered shopper can do.*   
   All of the features and functionality above are certainly also available and accessible for registered / logged-in users.   

2. *Easily log in or log out.*  
   Logged-in users can log out by clicking the user icon on the left side of the Navbar.  
   ![Logout link](readme-testing-files/testing/user-stories/logout-link.png "Logout link")      

3. *Easily recover my password in case I forget it.*   
   On the Log In page, there's an option to change your password below the buttons. When clicked, it will lead the users to the password reset page.   
   ![Password reset](readme-testing-files/testing/user-stories/password-reset.png "Password reset")      

4. *Receive an email confirmation after registering.*   
   After successfully registering to the website, users then will be informed to check their inbox.  
   ![Email verification 1](readme-testing-files/testing/user-stories/email-verify-1.png "Email verification 1")      
   In the user's inbox, an email from Shoes And More is found. Users then will be asked to verify their email by clicking the link provided.  
   ![Email verification 2](readme-testing-files/testing/user-stories/email-verify-2.png "Email verification 2")      
   After the link is clicked, users then will be directed back to the website, and to confirm the email address.   
   ![Email verification 3](readme-testing-files/testing/user-stories/email-verify-3.png "Email verification 3")      

5. *Have a personalized user profile where I can see my order history and change my information.*    
   By navigating to the My Account in the Navbar (or user icon on mobile), and clicking on My Profile, users can see their profile page. This page is divided into 3 pills/tabs - My Information, My Purchases, and Ratings/Reviews. Users can see/update their delivery information and see their order history by clicking the My Information pill and My Purchases pill respectively.   
   ![Update information](readme-testing-files/testing/user-stories/profile-information.png "Update information")   
   ![Order history](readme-testing-files/testing/user-stories/profile-orderhistory.png "Order history")    

6. *Review products that I have purchased before.*   
   Users can review the products that they have already purchased before by navigating to the Ratings/Reviews pill on the My Profile page.  
   ![Products to be reviewed](readme-testing-files/testing/user-stories/profile-reviews.png "Products to be reviewed")   
   By clicking the Give Review button, users will be directed to the Add Review page.   
   ![Add review](readme-testing-files/testing/user-stories/add-review.png "Add review")  

7. *Edit and delete my reviews.*  
   Once users submit a review, they can view the review by navigating to the Individual Product page in the Reviews section. If the user owns the review, there will be two buttons available under the review - the Edit button and Delete button.  
   ![Review](readme-testing-files/testing/user-stories/review.png "Review")  

   When the Edit button is clicked, the user will be directed to the Edit Review page, which has a similar layout to the Add Review page. The only difference is, on Edit Review, the input rating and review are already pre-populated with the existing review. Users can submit the updated review by clicking the 'Submit Review' button.   
   ![Edit review](readme-testing-files/testing/user-stories/edit-review.png "Edit review")   

   When the Delete button is clicked, a modal will show up to confirm users if they really want to delete their review. To confirm, click the 'Yes, Delete button.  
   ![Modal to delete review](readme-testing-files/testing/user-stories/modal-delete-review.png "Modal to delete review")  

8. *Add products to the wishlist, so I can quickly find products I'd like to purchase.*  
   Users can add products to their favorites by clicking the heart icon on the top-right of each product. This heart icon then turned red if the product is in the user's favorites.  
   ![Heart icon to add to favorites](readme-testing-files/testing/user-stories/heart-icon.png "Heart icon to add to favorites")    

9. *Remove products from the wishlist, so I can remove products I don't wish to purchase.*  
10. *Easily put the wishlist products into the shopping bag.*   
   By clicking the Favorites link on the Navbar (heart icon on mobile's Navbar, the user can navigate to the Favorites page to view all products the user has added to favorites. Users can remove products from the Favorites by clicking the Trash-can icon on the top-right of each product. Users can also directly add the product to the shopping bag by choosing a size and then clicking on the 'Add to Bag' button.   
   ![Favorites](readme-testing-files/testing/user-stories/favorites.png "Favorites")    


### C. As an admin and store management, I want to be able to:
1. *Add a product.*   
   Admin can add a product to the website by logging in as admin, navigating to My Account, and choosing Product Management. Admin then will be directed to the Add Products page. After filling out the form, they can click the 'Add Product' button.   
   ![Add product](readme-testing-files/testing/user-stories/add-product.png "Add product")   

2. *Edit or update a product.*   
   Admin can edit a product by logging in as admin, navigating to the Products page or the Individual Product page, and clicking on the Edit link.  
   ![Edit and Delete product](readme-testing-files/testing/user-stories/admin-edit-delete.png "Edit and Delete product")   

   Admin then will be directed to the Edit Products page. After filling out the form, they can click the 'Edit Product' button.  
   ![Edit product](readme-testing-files/testing/user-stories/edit-product.png "Edit product")   

3. *Delete a product.*   
   Admin can delete a product by logging in as admin, navigating to the Products page or the Individual Product page, and clicking on the Delete link. A modal will then show up to confirm the deletion. Admin can confirm it by clicking on the 'Yes, Delete button.  
   ![Edit and Delete product](readme-testing-files/readme/delete-product-modal.png "Edit and Delete product")   


[Back to top &uarr;](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#shoes-and-more---testing)  

<br/>  

## **2. Auto Prefixer CSS**   
[Autoprefixer CSS](https://autoprefixer.github.io/) was used to add CSS vendor prefixes to the CSS rules after the developing process was done, to ensure that they work across all browsers.  

<br/>  

## **3. Manual Testing by The Developer**  
### **Browsers Compatibility**   
The website was tested through the following browsers: Google Chrome, Microsoft Edge, Opera, Mozilla Firefox, and Safari (iOS) browsers.  

### **Devices**  
The website was also viewed on the following devices:  
- Windows Desktop  
- Windows Laptop  
- Tablets: iPad Mini 2 and iPad 2018  
- Mobile: iPhone7, iPhone 8, iPhone 12 Mini, Asus Zenfone Max Pro M2, and LG G5
- Friends and family members were asked to review the site on their devices and to point out any bugs and/or user experience issues.  

### **Responsiveness**   
To check the responsiveness of the website across all devices, the developer tools are used regularly during the developing process. The website is still responsive for devices as small as 320px wide.  
 

### **Links**   
All links and buttons were tested to ensure that:  
- All navigation links are linking correctly and working as expected.    
- The social media buttons are working and opening in a new tab.  

**Result**: All of the links and buttons are working properly.  
![Links manual testing](readme-testing-files/testing/links-test.png "Links manual testing")   



### **Forms**  
The form was also tested to ensure that:  
- For a few forms such as Edit Review, Edit Product, Checkout, and User Profile Information form, the fields are automatically filled out/prepopulated with the existing data (if the data is available). 
- The required attributes are working.  
- There's a validation message that explains the correct format if the user filled in the wrong format (for username and password).  
- Submit and Cancel/ Back buttons work as expected.  
- Datas are saved into the database.  
- Toast message informs feedback after submitting the form.  

**Result**: All of the links and buttons are working properly.   

![Forms manual testing](readme-testing-files/testing/forms-test.png "Forms manual testing")  

[Back to top &uarr;](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#shoes-and-more---testing)  

<br/>

## **HTML & CSS Validator Testing**  
I planned to do the HTML using the W3C Validator, but unfortunately on the day that I did this testing (Feb 27th, 2022), the W3C was offline the whole day. Due to time constraints (the deadline for this project was Feb 28th, 2022), I decided to use another HTML Validator.  

### HTML   
According to [W3C Wiki](https://www.w3.org/wiki/Validating_your_HTML?TB_iframe=true), [Validator.nu (X)HTML5 Validator](https://html5.validator.nu/) is the recommended validator if using HTML5. I decided to use this as a replacement to the usual W3C Markup Validator, to validate the website on the HTML part. These are the errors and warnings I got:   
![HTML Validator testing](readme-testing-files/testing/html-validator.png "HTML Validator testing")  
After fixing all the warnings and errors, all pages passed the Validator. Below are the screen capture of the result for every pages.  
- [Homepage (index.html)](readme-testing-files/testing/html-validator/home.png)   
- [Products Page (products.html)](readme-testing-files/testing/html-validator/products.png)   
- [Individual Product Page (product_detail.html)](readme-testing-files/testing/html-validator/individual-product.png)      
- [Add Product Page (add_product.html)](readme-testing-files/testing/html-validator/add-product.png)   
- [Edit Product Page (edit_product.html)](readme-testing-files/testing/html-validator/edit-product.png)   
- [Shopping Bag Page (bag.html)](readme-testing-files/testing/html-validator/shopping-bag.png)   
- [Checkout Page (checkout.html)](readme-testing-files/testing/html-validator/checkout.png)   
- [Checkout Success Page (checkout_success.html)](readme-testing-files/testing/html-validator/checkout-success.png)   
- [Favorites Page (favorites.html)](readme-testing-files/testing/html-validator/favorites.png)   
- [Profile Page (profile.html)](readme-testing-files/testing/html-validator/profile.png)   
- [Add Review Page (add_review.html)](readme-testing-files/testing/html-validator/add-review.png)   
- [Edit Review Page (edit_review.html)](readme-testing-files/testing/html-validator/edit-review.png)   
- [Articles Page (articles.html)](readme-testing-files/testing/html-validator/articles.png)   
- [Individual Article Page (article.html)](readme-testing-files/testing/html-validator/individual-article.png)   
- [Contact Page (contact.html)](readme-testing-files/testing/html-validator/contact.png)   
- [FAQ Page (faq.html)](readme-testing-files/testing/html-validator/faq.png)   

### CSS   
Fortunately, [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) was back online just on time. All CSS pages passed the validator, with no errors found. However, there were warnings concerning the vendor prefixes added by Autoprefixer CSS. I decided to ignore the warnings because the vendor prefixes are important to ensure that the styling works across different browsers.  
Here is the result for each CSS file.  
- ```base.css```   
   ![base.css validation](readme-testing-files/testing/css-validator/base-css.png "base.css validation")  
- ```checkout.css```   
   ![checkout.css validation](readme-testing-files/testing/css-validator/checkout-css.png "checkout.css validation")  
- ```contact.css```   
   ![contact.css validation](readme-testing-files/testing/css-validator/contact-css.png "contact.css validation")   
- ```profiles.css```   
   ![profiles.css validation](readme-testing-files/testing/css-validator/profile-css.png "profiles.css validation")  
- ```reviews.css```   
   ![reviews.css validation](readme-testing-files/testing/css-validator/reviews-css.png "reviews.css validation")  

[Back to top &uarr;](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#shoes-and-more---testing)  

<br>

## JavaScript Testing   
I ran the javascript code through [JSHint](https://jshint.com/), and there were some warnings about missing semicolons - which now have been fixed, and one undefined variable: ```Stripe```. We know that ```Stripe``` is an external variable from the Stripe Payment that we use on the website, so it's not defined inside the JS file.  
See below the screen capture of the testing result.  
- [stripe_elements.js](readme-testing-files/testing/js-hint/stripe-elements-js.png)    
- [products.js](readme-testing-files/testing/js-hint/products-js.png)    
- [reviews.js](readme-testing-files/testing/js-hint/review-js.png)    
- [profiles.js](readme-testing-files/testing/js-hint/profiles-js.png)    

<br/>  

## Flake8 and Pep8-Online Testing  
Using Flake8 python linting on Gitpod, I have fixed almost all problems.  

Still existing problems:
- On apps.py in checkout app : 
   Problem: ```'checkout.signals' imported but unused```  
   Explanation: It is to be imported, but the linting doesn't know that yet and so throws an error. I decided to ignore this error.  
- On webhooks.py in checkout app:
   Problem: ```local variable 'e' is assigned to but never userd```   
   Explanation: The lint was catching too general exception Exception (broad-except). I decided to ignore this error.
- On settings.py in project's folder:
   Problem: ```line too long (91 > 79 characters)```
   ```
   AUTH_PASSWORD_VALIDATORS = [
      {
         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
   ] 
   ```   
   Explanation: I decided to ignore this problem as the lines couldn't be broken down without breaking the password validation functionality.   
   
All other warnings, errors, and problems on Gitpod's flake 8 are resolved.   

To add more validation to the code, I also used [Pep8 Online](http://pep8online.com/checkresult), and all codes passed the PEP8 requirements.  

<br/>

## **Lighthouse Testing**   
Page | Performance | Accessibility | Best Practices | SEO  
---|---|---|---|---
Home Page | 95 | 87 | 92 | 100   
Products Page | 86| 91 | 100 | 100   
Individual Product Page | 98 | 84 | 100 | 100   
Shopping Bag Page | 97 | 90 | 100 | 90   
Checkout Page | 91 | 89 | 100 | 100   
Checkout Success Page | 98 | 91 | 100 | 100   
Profiles Page | 86 | 91 | 100 | 100   
Add Review Page | 98 | 89 | 100 | 100   
Edit Review Page | 98 | 89 | 100 | 100   
Favorites Page | 95 | 91 | 100 | 100 
Articles Page | 95 | 89 | 100 | 100    
Individual Article Page | 98 | 91 | 100 | 100     
Contact Page | 99 | 88 | 100 | 100   
FAQ Page | 99 | 88 | 100 | 100    
Add Product Page | 99 | 81 | 100 | 100    
Edit Product Page | 99 | 82 | 100 | 100  

I have taken these steps to improve the performance based on the suggestions from Lighthouse:   
- Add an aria-label to buttons that are using only icons without text.  
- Add labels to form elements that didn't have labels yet.  

[Back to top &uarr;](https://github.com/dissyulina/shoesandmore/blob/main/TESTING.md#shoes-and-more---testing)  
