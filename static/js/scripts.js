document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Product added to cart: ' + this.closest('.product-item').querySelector('h3').innerText);
        });
    });
});
