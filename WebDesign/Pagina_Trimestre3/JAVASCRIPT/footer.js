function Footer() {
    return (
    <footer>
        <section class="sec-1">
            <div class="div-1-logo">
                <img src="../IMAGENS/menu_and_footer/logo-v2.png" alt="Logo Catppuccino"/>
            </div>
            <div class="div-2-contact">
                <div>
                    <h2>Contact</h2>
                    <hr/>
                </div>
                <ul>
                <li>Jessica Mayumi</li>
                <li>+1(098) 765-4321</li>
                <li>uwu.jessyca@gmail.com</li>
                </ul>
            </div>
            <div class="div-3-about">
                <div>
                    <h2>About</h2>
                    <hr/>
                </div>
                <ul>
                    <li><a href="#">Terms of use</a></li>
                    <li><a href="#">Media</a></li>
                    <li><a href="#">Events</a></li>
                </ul>
            </div>
        </section>
        <section class="sec-2">
            <ul>
                <li><a href="#"><img src="../IMAGENS/menu_and_footer/instagram.png" alt="#"/></a></li>
                <li><a href="#"><img src="../IMAGENS/menu_and_footer/twitter.png" alt="#"/></a></li>
                <li><a href="#"><img src="../IMAGENS/menu_and_footer/youtube.png" alt="#"/></a></li>
                <li><a href="#"><img src="../IMAGENS/menu_and_footer/facebook.png" alt="#"/></a></li>
            </ul>
        </section>
    </footer>
    );
}

ReactDOM.render(<Footer />, document.getElementById('footer'))