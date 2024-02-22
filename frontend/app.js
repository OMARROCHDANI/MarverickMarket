fetch("http://127.0.0.1:8000/api/products/")
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    const container = document.getElementById("product-container");

    data.forEach((product) => {
      const markup = `
        <div class="product-card">
          <img src="${product.photo}" alt="" />
          <h4>${product.name}</h4>
          <div>
            <span>$${product.price}</span>
            <button>+</button>
          </div>
        </div>
      `;

      // Append the markup to the container
      container.innerHTML += markup;
    });
  })
  .catch((error) => console.log(error));
