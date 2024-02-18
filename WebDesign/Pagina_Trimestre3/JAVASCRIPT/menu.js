function Menu() {
    return (
            <nav>
            <a href="../index.html"><img class="img-logo" src="../IMAGENS/menu_and_footer/logo-v1.png" alt="Logo"/></a>
                <a href="../index.html">home</a>
                <div class="dropdown">
                    <a class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">menu</a>
                    <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="../HTML/coffee.html">coffee</a></li>
                    <li><a class="dropdown-item" href="../HTML/page_under_construction.html">cake and pie</a></li>
                    <li><a class="dropdown-item" href="../HTML/page_under_construction.html">breakfast</a></li>
                    <li><a class="dropdown-item" href="../HTML/page_under_construction.html">offers</a></li>
                    </ul>
                </div>
                <a href="../HTML/page_under_construction.html">contact</a>
                <a href="../HTML/login.html">account <img src="/IMAGENS/menu_and_footer/user.png" alt="user"/></a>
                <div class="shopping-container">
                    <div class="counter-container">
                    <span id="counter">0</span>
                    <a href="../HTML/page_under_construction.html"><img src="../IMAGENS/menu_and_footer/cart.png" alt="Cart"/></a>
                    </div>
                </div>
            </nav>
    );
}


//ReactDOM.render(<Menu />, document.getElementById('menu'))

const root = ReactDOM.createRoot(document.getElementById('menu'));
root.render(<Menu/>);