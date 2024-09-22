import { FormEvent, useEffect, useState } from "react";
import AuthorizationService from "../../services/AuthorizationService";
import { useNavigate } from "react-router-dom";

function LoginPage() {

    const [ email, setEmail ] = useState<string>();
    const [ password, setPassword ] = useState<string>();
    const [ authService, setAuthService ] = useState<AuthorizationService>();
    const [ isPending, setPending ] = useState<boolean>(false);
    const [ error, setError ] = useState<Error | null>(null);
    const navigate = useNavigate();

    useEffect( () => {
        
        const authService = AuthorizationService.getAuthorizationService();
        setAuthService(authService);

    }, [])

    function login(formEvent: FormEvent) {
        
        formEvent.preventDefault();

        setError(null);
        setPending(true);

        authService?.authorizeUser(email!, password!)
        .then( () => {
            setPending(false);
            navigate('/');
            
        })
        .catch( (err) => {
            setPending(false);
            console.log(err);
            setError(err);
        })
    }

    function loginViaGoogle() {

        authService?.oauthSignIn()
    }

    return (
        <div className="d-flex align-items-center flex-column">

            <form onSubmit={login} className="w-50 d-flex align-items-center flex-column p-5 bg-dark m-3 rounded shadow">
                <input type='text' name="email" id='emailInput' className="form-control mt-4 p-2"
                 value={email} placeholder="email" onChange={ (e) => {setEmail(e.target.value)} }/>

                <input type='password' name="password" id='passwordInput' className="form-control mt-4 p-2"
                 value={password} placeholder="password" onChange={ (e) => setPassword(e.target.value) } />

                <button type="submit" className="btn btn-primary mt-4"> Submit </button>
            </form>


            <button className="btn btn-info mt-4" onClick={loginViaGoogle}> Login via Google </button>


            {isPending && <h1 className="text-center">Loading...</h1>}
            {error && <h3 className="text-center">Something was wrong</h3>}
        </div>
        
    );
}

export default LoginPage