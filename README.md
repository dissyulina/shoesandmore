# **Shoes And More**
![Shoes and More website in variouse devices](readme-testing-files/readme/main-image.png "Shoes and More website in variouse devices")  

[View live website here]()

</br>  

**Table of Contents**   


------

## **Introduction**   
Welcome to Shoes and More website!
Shoes and More is an e-commerce website that sells shoes and accessories (bags, wallets, etc). It's completed with authentication mechanism and stripe payments to allow users to safely purchased products from the site.  

Please note that this website was created for the Code Institute’s Milestone Project 4 as part of their Diploma in Full Stack Software Development. The requirements are to make a full-stack website, using HTML, CSS, JavaScript, Django+Python, relational database, stripe payments, and other additional libraries as needed.  

<br/>  

## **UX Development Plane**   
### **1. Strategy Plane**  
#### **Project Goals**   
The primary goal of this project is to create an e-commerce website that works perfectly, is visually appealing in design, and intuitive for a first time user. It allows user to perform not only the basic functionalities in an e-commerce website (such as sign up/ log in, ability to purchase items and perform payments), but also to ensure that users have a great experience and more interactivity within the site through additional functionalities such as put items into their wishlist, and write reviews, and reading articles.  

#### **User Goals**  
The user is looking for:
- An online store / website that is straightforward and intuitive to use, easy to navigate and to make a purchase on the site. 
- An online store/ website where the user can have other additional activities and engage more store.  

The target user for this site is:
- Young adult, between 18 - 40
- Fun, fashionable people
- People who enjoy the convenience of using technology and social media


#### **Site Owner Goals**  
The site owner is looking to:
- Be able to make money by providing products (and services) to the users. 
- Manage products in the website.



#### **User Stories** 
- As a shopper I want to be able to:
   1. Quickly identify what products/services the site sells.  
   2. Quickly identify deals and special offers.   
   3. Search for a product.   
   4. Identify a glimpse of most populars products.   
   5. View all products, and easily navigate between categories.  
   6. Sort by price, by rating, and by color.   
   7. View individual product's page and read the relevant information.  
   8. Read a product's review.  
   9. Easily select size and quantity of the product, and add it to shopping bag.  
   10. View the shopping bag with products added in it.  
   11. Update the shopping bag by adjusting the quantity of the products, or removing them from the shopping bag.  
   12. Checkout and easily enter my payment information.  
   13. Feel my personal and payment information is safe and secure.  
   14. View an order confirmation after purchasing.  
   15. Receive an email confirmation after purchasing.  
   16. Read relevant articles/ blogs about shoes or accessories.  
   17. Easily navigate within the site, through Navigation Bar and Footer.  
   18. Easily register for an account.  
   19. Find FAQ section for my questions.  
   20. Contact the shop via a contact form.    

- As a registered user/ shopper, I want to be able to:
   1. Access all functionalities that an unregistered shopper can do.  
   2. Easily login or logout.  
   3. Easily recover my password in case I forget it.  
   4. Receive an email confirmation after registering.  
   5. Have a personalized user profile where I can see my order history and change my information.  
   6. Review products that I have purchased before.  
   7. Edit and delete my reviews.  
   8. Add products to the wishlist, so I can quickly find products I'd like to purchase. 
   9. Remove products from the wishlist, so I can remove products I don't wish to purchase.
   9. Easily put the wishlist products into the shopping bag.   

- As an admin and store management, I want to be able to:
   1. Add a product.  
   2. Edit or update a product.  
   3. Delete a product.  

<br/>  

### **2. Scope Plane**  
Based on all goals and user stories, a scope was defined for the site with room for future improvements.  

#### **Functional Requirements**  
The unregistered users will be able to:
- Sign up to the site by providing username, email, and password.  
- View all products and sort them by price, rating, and color.
- Search for products
- View product's detail.
- Add products to the shopping bag.
- Update and remove items in the shopping bag.
- Checkout and make a payment.
- Receive email confirmation of the transaction.  

The registered users will be able to:
- Do all things that unregistered users able to do. 
- Log in to the site by providing username and password.
- View profile page.
- Update delivery / contact information on their profile page.
- View order history on their profile page.
- Write reviews for products that they have purchased.
- Edit those reviews.
- Delete those reviews.
- Add products to their wishlist.
- Remove products from wishlist.  

The admin/ site owners will be able to:
- Have all functionalities as a registered user.  
- Add a product to the site.  
- Edit or update a product.  
- Delete a product.  

#### **Non-functional Requirements**  
Users will be able to:
- View articles/ blogs about shoes, accessories, and fashion in general.
- View FAQ page to find answers for their questions.
- Send message to the store via contact form.
- Navigate easily and intuitively throughout the site.  

<br/>  

### **3. Structure Plane**  
The website was organized in a Hierarchical Tree Structure that ensures the user can navigate easily and intuitively. Below is the website workflow (was designed using [Creately](https://creately.com/)).  

![The website's structure](readme-testing-files/readme/structure.png "The website's structure")   
There's a clear page access separation between unregistered users and registered user. While unregistered users can still purchase products and receive the confirmation via email, they are not able to:
- View their order history
- Give reviews (and edit or delete their reviews accordingly)  
- Make a favorite list of products.  

Those features mentioned are available for registered users.

<br/>  

### **4. Skeleton Plane**  
Wireframes were created using Figma to design the navigation and interface of the website. The wireframes were created only for desktop, which then will be transformed to high fidelity mock-ups in various device sizes (see Surface Plane). 

- [Wireframe for Home page](readme-testing-files/readme/wireframes/wireframe-home.png) 
- [Wireframe for Products page](readme-testing-files/readme/wireframes/wireframe-products.png)  
- [Wireframe for Individual Product page](readme-testing-files/readme/wireframes/wireframe-individual-product.png)  
- [Wireframe for Favorites page](readme-testing-files/readme/wireframes/wireframe-favorites.png)  
- [Wireframe for Shopping Bag page](readme-testing-files/readme/wireframes/wireframe-shoppingbag.png)  
- [Wireframe for Checkout page](readme-testing-files/readme/wireframes/wireframe-checkout.png)  
- [Wireframe for Profile page (Update user's information)](readme-testing-files/readme/wireframes/wireframe-profile-updateinfo.png)  
- [Wireframe for Profile page (View order history)](readme-testing-files/readme/wireframes/wireframe-profile-orderhistory.png)  
- [Wireframe for Profile page (Reviews)](readme-testing-files/readme/wireframes/wireframe-profile-reviews.png)  
- [Wireframe for Articles page](readme-testing-files/readme/wireframes/wireframe-articles.png)  
- [Wireframe for Individual Article page](readme-testing-files/readme/wireframes/wireframe-individual-article.png)  
- [Wireframe for Contact page](readme-testing-files/readme/wireframes/wireframe-contact.png)  
- [Wireframe for Add / Edit Review page](readme-testing-files/readme/wireframes/wireframe-add-edit-review.png)  
- [Wireframe for Sign Up page](readme-testing-files/readme/wireframes/wireframe-signup.png)  
- [Wireframe for Log In page](readme-testing-files/readme/wireframes/wireframe-login.png)  

<br/>  

### **5. Surface Plane**  
High fidelity mock-ups were created using Figma as well for a better and clearer visualization before coding, and also to check if the color scheme and images match and work great together. This has allowed the developer to concentrate solely on the development part (front end and back end), as the design has already made with such details. The high fidelity mock-ups were created in three different device sizes - desktop, tablet, and mobile.  

- [High Fidelity Mock-up for Home page](readme-testing-files/readme/high-fidelity-mockups/mockup-home.png)  
- [High Fidelity Mock-up for Products page](readme-testing-files/readme/high-fidelity-mockups/mockup-products.png)  
- [High Fidelity Mock-up for Individual Product page](readme-testing-files/readme/high-fidelity-mockups/mockup-individual-product.png)  
- [High Fidelity Mock-up for Favorites page](readme-testing-files/readme/high-fidelity-mockups/mockup-favorites.png)  
- [High Fidelity Mock-up for Shopping Bag page](readme-testing-files/readme/high-fidelity-mockups/mockup-shoppingbag.png)  
- [High Fidelity Mock-up for Checkout page](readme-testing-files/readme/high-fidelity-mockups/mockup-checkout.png)  
- [High Fidelity Mock-up for Profile page (Update user's information)](readme-testing-files/readme/high-fidelity-mockups/mockup-profile-updateinfo.png)  
- [High Fidelity Mock-up for Profile page (Order History)](readme-testing-files/readme/high-fidelity-mockups/mockup-profile-orderhistory.png)  
- [High Fidelity Mock-up for Profile page (Reviews)](readme-testing-files/readme/high-fidelity-mockups/mockup-profile-reviews.png)  
- [High Fidelity Mock-up for Articles page](readme-testing-files/readme/high-fidelity-mockups/mockup-articles.png)  
- [High Fidelity Mock-up for Individual Article page](readme-testing-files/readme/high-fidelity-mockups/mockup-individual-article.png)  
- [High Fidelity Mock-up for Contact page](readme-testing-files/readme/high-fidelity-mockups/mockup-contact.png)  
- [High Fidelity Mock-up for Add / Edit Review page](readme-testing-files/readme/high-fidelity-mockups/mockup-add-edit-review.png)  
- [High Fidelity Mock-up for Sign Up page](readme-testing-files/readme/high-fidelity-mockups/mockup-signup.png)  
- [High Fidelity Mock-up for Log In page](readme-testing-files/readme/high-fidelity-mockups/mockup-login.png)  

#### **Color Scheme**  
The overall color-theme of the website was natural earthy colors, which have relaxing and comforting influences, and encourages feelings of warmth and calmness. Using [Coolors](https://coolors.co), I started with beige (#E8DCD5) and brown (#644536), and generated one more color that compliments them both - the result was a salmon color (#B2675E). I also found a hero image that fits the overal theme and colors accordingly.   
![The color scheme](readme-testing-files/readme/color-scheme.png "The color scheme")  

#### **Typography**  
All of the fonts were sourced from [Google Fonts](https://fonts.google.com).   
- Main font: Noto Sans   
   Noto Sans is a sans-serif font, used as the main font, for all paragraphs and buttons. Open Sans was chosen because it has a modern and clean style. 
- Secondary font: DM Serif Display    
   DM Serif Display is a serif font, used as the headers font on the Home page, in order to contrast them with serif font.  


#### **Imagery**  

