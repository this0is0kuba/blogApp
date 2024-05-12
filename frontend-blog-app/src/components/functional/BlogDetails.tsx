import Blog from "../../models/Blog";

function BlogDetails({blog} : {blog: Blog}) {
    return (
        <div>
            <h2>Blog Details</h2>
            <span>{blog.title}</span>
        </div>
    );
}

export default BlogDetails;