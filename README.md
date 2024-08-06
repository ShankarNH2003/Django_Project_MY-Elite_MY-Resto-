

    <h1>Django_Project_MY-Elite_MY-Resto</h1>

    <h2>Overview</h2>
    <p><strong>Django_Project_MY-Elite_MY-Resto</strong> is a restaurant management system built using the Django framework. This project aims to streamline restaurant operations by providing features for managing food items, orders, reservations, and user accounts. It includes functionalities for both customers and restaurant employees, ensuring an efficient and seamless dining experience.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication:</strong> Separate authentication for employees and customers, including registration, login, and profile management.</li>
        <li><strong>Food Management:</strong> Manage food categories and items, with options to add, edit, and remove items.</li>
        <li><strong>Ordering System:</strong> Customers can browse the menu, add items to their cart, and place orders.</li>
        <li><strong>Cart Management:</strong> View cart details, adjust quantities, and proceed to checkout.</li>
        <li><strong>Reservation System:</strong> Book tables and rooms online, check availability, and manage reservations.</li>
        <li><strong>Order History:</strong> View and manage order history for customers and employees.</li>
        <li><strong>Payment Integration:</strong> Various payment methods to handle transactions securely.</li>
    </ul>

    <h2>Installation</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>Django 4.x</li>
        <li>Pip (Python package installer)</li>
    </ul>

    <h3>Steps</h3>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/yourusername/Django_Project_MY-Elite_MY-Resto.git
cd Django_Project_MY-Elite_MY-Resto</code></pre>
        </li>
        <li><strong>Create and Activate a Virtual Environment</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Apply Migrations</strong>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li><strong>Create a Superuser</strong>
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li><strong>Run the Development Server</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Open Your Browser</strong>
            <p>Navigate to <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a> to view the application.</p>
        </li>
    </ol>

    <h2>Project Structure</h2>
    <ul>
        <li><strong>main/</strong> - Contains core functionality for managing food items, orders, reservations, and user profiles.</li>
        <li><strong>cart/</strong> - Handles cart operations and order placements.</li>
        <li><strong>payment/</strong> - Manages payment processing and transactions.</li>
        <li><strong>templates/</strong> - HTML templates for rendering pages.</li>
        <li><strong>static/</strong> - Static files such as CSS and JavaScript.</li>
    </ul>

    <h2>Configuration</h2>
    <p>Configuration settings are located in <code>settings.py</code>. Update the following as needed:</p>
    <ul>
        <li><strong>DATABASES:</strong> Configure your database settings.</li>
        <li><strong>STATICFILES_DIRS:</strong> Update paths for static files.</li>
        <li><strong>TEMPLATES_DIR:</strong> Update paths for template files.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Please follow these steps to contribute:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Make your changes and commit (<code>git commit -am 'Add new feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Create a pull request.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contact</h2>
    <p>For any questions or support, please contact:</p>
    <ul>
        <li>Email: <a href="mailto:shankarhulagur1003@gmail.com">contact@myeliteresto.com</a></li>
    </ul>

    <h2>Screenshots</h2>

    <h3>Main Page</h3>
    <img src="https://github.com/user-attachments/assets/c5e27f9f-7e20-4dc0-864f-94d1d4b6aa30" alt="Main Page" style="max-width: 100%; height: auto;">

    <h3>Menu Page</h3>
    <img src="https://github.com/user-attachments/assets/a59f885f-987a-4a09-80e7-f00631091714" alt="Menu Page" style="max-width: 100%; height: auto;">

    <h3>Cart Page</h3>
    <img src="https://github.com/user-attachments/assets/298199ea-f39e-4b61-b23f-95ae377786c9" alt="Cart Page" style="max-width: 100%; height: auto;">

    <h3>Checkout Page</h3>
    <img src="https://github.com/user-attachments/assets/3ea782c5-dd5c-4c92-9e0b-3b7b221a681b" alt="Checkout Page" style="max-width: 100%; height: auto;">

    <h3>Order Confirmation Page</h3>
    <img src="https://github.com/user-attachments/assets/6a11eb83-e010-4851-a5f2-0b35cfa456e3" alt="Order Confirmation Page" style="max-width: 100%; height: auto;">

    <h3>Reservation Page</h3>
    <img src="https://github.com/user-attachments/assets/71e9a98c-d01e-4c18-9269-b36bc284803c" alt="Reservation Page" style="max-width: 100%; height: auto;">

    <h3>User Profile Page</h3>
    <img src="https://github.com/user-attachments/assets/fd72308b-0cf1-446d-9f35-fa97b847db3e" alt="User Profile Page" style="max-width: 100%; height: auto;">

    <h3>Admin Dashboard</h3>
    <img src="https://github.com/user-attachments/assets/8c1e0005-b062-450a-9d1e-5c000f16c53b" alt="Admin Dashboard" style="max-width: 100%; height: auto;">


