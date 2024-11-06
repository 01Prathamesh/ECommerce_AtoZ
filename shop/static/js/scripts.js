document.addEventListener('DOMContentLoaded', function() {
    // Initialize cart count when the page loads
    updateCartIcon();

    // Add event listener to 'Add to Cart' buttons
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');  // Get the product ID from button's data attribute
            const productName = this.closest('.product-item').querySelector('h3').innerText;  // Get the product name
            addToCart(productId, productName);  // Add product to cart
        });
    });

    // Function to add item to cart in localStorage
    function addToCart(productId, productName) {
        // Get the cart from localStorage (or initialize as empty array if not present)
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        
        // Check if the product already exists in the cart
        const existingProduct = cart.find(item => item.productId === productId);
        
        if (existingProduct) {
            // If the product is already in the cart, increment its quantity
            existingProduct.quantity++;
        } else {
            // If not, add it to the cart with quantity 1 and product name
            cart.push({ productId, productName, quantity: 1 });
        }
        
        // Save the updated cart back to localStorage
        localStorage.setItem('cart', JSON.stringify(cart));

        // Optionally, show a confirmation message to the user
        alert(`Product added to cart: ${productName}`);

        // Update the cart icon and count
        updateCartIcon();
    }

    // Function to update the cart icon and display cart count
    function updateCartIcon() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);  // Total items in cart
        
        // Update the UI (assumes you have an element with id 'cart-count')
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = cartCount;  // Display total number of items
        }

        // Optionally, show a message or update a cart icon to reflect cart count
        if (cartCount > 0) {
            cartCountElement.style.display = 'inline';  // Show the cart count if items exist
        } else {
            cartCountElement.style.display = 'none';  // Hide cart count if empty
        }
    }
});
