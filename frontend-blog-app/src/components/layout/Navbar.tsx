function Navbar() {
    return (

        <nav className="navbar bg-dark border-bottom border-body px-4 py-3 sticky-top" data-bs-theme="dark">
                    
            <h3 className="text-light">Word Weave</h3>

            <div className="links">

                <a href="/" className="btn btn-dark">Home</a>
                <a href="/blogs" className="ms-2 btn btn-dark">Blogs</a>
                <a href="/yourBlogs" className="ms-2 btn btn-dark">Your Blogs</a> 
                <a href="/create" className="ms-2 btn btn-dark">New Blog</a>
                <a href="/manage" className="ms-2 btn btn-dark">Manage</a>
                <a href="/profil" className="ms-2 btn btn-dark">Account</a>
            </div>

            <form className="d-flex" role="search">
                <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
                <button className="btn btn-outline-success" type="submit">Search</button>
            </form>
            
        </nav>
    );
}

export default Navbar;