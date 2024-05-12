import { Link } from "react-router-dom";

function Navbar() {
    return (

        <nav className="navbar bg-dark border-bottom border-body px-4 py-3 sticky-top" data-bs-theme="dark">
                    
            <h3 className="text-light">Word Weave</h3>

            <div className="links">

                <Link to="/" className="btn">Home</Link>
                <Link to="/blogs" className="ms-2 btn btn-dark">Blogs</Link>
                <Link to="/yourBlogs" className="ms-2 btn btn-dark">Your Blogs</Link> 
                <Link to="/create" className="ms-2 btn btn-dark">New Blog</Link>
                <Link to="/manage" className="ms-2 btn btn-dark">Manage</Link>
                <Link to="/profil" className="ms-2 btn btn-dark">Account</Link>
            </div>

            <form className="d-flex" role="search">
                <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
                <button className="btn btn-outline-success" type="submit">Search</button>
            </form>
            
        </nav>
    );
}

export default Navbar;