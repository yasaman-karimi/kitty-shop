### Template
- Get a template from gpt or search on web for website (you can use bootstrap)
- Have a reasonable template hierarchy
- Have a side bar, filled with user data (or whatever you want)
- If you need to share some data between all your templates, check out template context providers
- Move your CSS into a seperate file and put it in statics

### Comment
- Add a comment form below products
- Show comments under products
- Add "is_verfied_buyer" and a "is_confirmed" fields to comment
- Only show comments with "in_confirmed" to true
- Mark those with "is_verified_buyer" with a nice tick mark
- Make sure we consider the comments in rating even if they're not confirmed

### Cart(Sabade kharid)
- Add a cart based on session or user
- Add "add to cart" to products
save products in session not in model
-learn about django session 
-if user is login save products in cart(model) if not save it in session 
m
