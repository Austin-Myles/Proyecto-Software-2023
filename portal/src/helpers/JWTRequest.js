import api from '@/helpers/api';
import router from '../router';
import { useToast } from 'vue-toastification';

const toast = useToast();

/* Should follow:
    route: string starting and ending with '/'
    returns: JSON object | error
*/
export async function getWithJWT(route) {
    try {
      const authToken = localStorage.getItem('token');
      const headers = {
        Authorization: `JWT ${authToken}`,
        'Content-Type': 'application/json',
      };

      const response = await api.get(route, { headers });
      return response;
    } catch (error) {
      if(error.response.status === 401) {
        localStorage.clear()
        router.push({ name: 'login' });
        toast.error('Debes iniciar sesion primero');
      }
      console.error("Error: " + error);
      return error;
    }
}

/* Should follow:
    route: string starting and ending with '/'
    body: JSON object
    returns: JSON object | error
*/
export async function postWithJWT(route, body) {
  try {
      const authToken = localStorage.getItem('token');

      const headers = {
          Authorization: `JWT ${authToken}`,
          'Content-Type': 'application/json',
      };
      const response = await api.post(route, body, { headers });

      return response;
  } catch (error) {
    if(error.response.status === 401) {
      localStorage.clear()
      router.push({ name: 'login' });
      toast.error('Debes iniciar sesion primero');
    }
    console.error("Error: " + error);
    return error;
  }
}
