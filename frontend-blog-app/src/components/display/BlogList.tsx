import { Link } from "react-router-dom";
import { Blog } from "../../models/Blog";

function BlogList({blogs}: {blogs: Blog[]}) {

    return (
        <div className="container pt-5">
            <div className="row">
                
                {
                    blogs.map( (blog) => (
                        <div className="col-4 my-3" key={blog.id}>
                            <div className="p-3 bg-dark h-100 rounded shadow-lg d-flex flex-column">
                                <h2>{blog.title}</h2>
                                <p className="text-secondary">{blog.content.slice(0, 150) + "..."}</p>
                                <div className="mt-auto d-flex justify-content-between">
                                    <div>
                                        <span>Creation date: </span>
                                        <span>{blog.creationDate}</span>
                                    </div>
                                    <Link className="btn btn-info" to={"/blogs/" + blog.id} >check</Link>
                                </div>
                            </div>
                        </div>
                    ))
                }

            </div>
        </div>
    );
}

export default BlogList;