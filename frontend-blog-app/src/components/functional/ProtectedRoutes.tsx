import { Navigate, Outlet } from "react-router-dom";
import AuthorizationService from "../../services/AuthorizationService";
import Token from "../../models/Token";

const ProtectedRoutes = () => {

    const authService: AuthorizationService = AuthorizationService.getAuthorizationService();
    const token: Token | null = authService.getToken();

    return token ? <Outlet/> : <Navigate to='/login'/>
}

export default ProtectedRoutes;