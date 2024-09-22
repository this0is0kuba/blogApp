import { useEffect, useState } from "react";
import AuthorizationService from "../../services/AuthorizationService";
import { useNavigate } from "react-router-dom";

function GoogleCallbackPage() {

    const [ authService, setAuthService ] = useState<AuthorizationService>();
    const navigate = useNavigate();

    useEffect( () => {
        
        const authService = AuthorizationService.getAuthorizationService();
        setAuthService(authService);

        parseToken();

    }, [])

    function parseToken() {

        const fragmentString = window.location.hash.substring(1);
        const params: {[key: string]: string} = {}
        const regex = /([^&=]+)=([^&]*)/g;

        let m: RegExpExecArray | null;

        while (m = regex.exec(fragmentString)) {
          params[decodeURIComponent(m[1])] = decodeURIComponent(m[2]);
        }

        if (Object.keys(params).length > 0 && params['state']) {

          if (params['state'] === window.localStorage.getItem('state')) {

            window.localStorage.setItem('oauth2Params', JSON.stringify(params) );
            console.log(params);

            navigate('/?success');

          } 
          else

            console.log('State mismatch. Possible CSRF attack');
            navigate('/login?fail');

        }
    }

    return (
        <div>
            <h3>Loading...</h3>
        </div>
    );
}

export default GoogleCallbackPage;