import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Blog } from "../../models/Blog";
import BlogService from "../../services/BlogService";
import BlogDetails from "./BlogDetails";

function BlogPage() {

    const { id } = useParams();

    const [blog, setBlog] = useState<Blog | null>(null);
    const [isPending, setPending] = useState<boolean>(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {

        const blogService = BlogService.getBlogService();

        blogService.getBlog(parseInt(id!))
            .then( (data: Blog) => {
                setBlog(data);
                setPending(false)
                setError(null);
            })
            .catch( (err: Error) => {
                setError(err);
                setPending(false);
            })

    }, [id]);
    
    return (
        <div>
            {error && <h2>{error.message}</h2>}
            {isPending && <h2>Loading...</h2>}
            {blog && <BlogDetails blog={blog} />}
        </div>
    );
}

export default BlogPage;