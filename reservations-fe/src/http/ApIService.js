import axios from 'axios';
// Change the API_URL to the correct location of the backend API before deploying the app
const API_URL = 'http://127.0.0.1:8000/'; /* 'http://localhost:8000' http://127.0.0.1:8000/
or 'http://yourPythonAnywhereName.pythonanywhere.com/'*/
export class APIService {
    constructor() {
    }

    getGuest(param_pk) {
        const url = `${API_URL}/api/guests/${param_pk}`;
        let jwtToken = localStorage.getItem('access');
        const headers = {Authorization: `JWT ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    getGuestList() {
        const url = `${API_URL}/api/guests/`;
        let jwtToken = localStorage.getItem('access');
        const headers = {Authorization: `JWT ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    addNewGuest(guest) {
        const url = `${API_URL}/api/guests/`;
        let jwtToken = localStorage.getItem('access');
        const headers = {Authorization: `JWT ${jwtToken}`};
        return axios.post(url, guest, {headers: headers});
    }

    updateGuest(guest) {
        const url = `${API_URL}/api/guests/${guest.pk}`;
        let jwtToken = localStorage.getItem('access');
        const headers = {Authorization: `JWT ${jwtToken}`};
        return axios.put(url, guest, {headers: headers});
    }

    deleteGuest(guest_Pk) {
        const url = `${API_URL}/api/guest/${guest_Pk}`;
        let jwtToken = localStorage.getItem('access');
        const headers = {Authorization: `JWT ${jwtToken}`};
        return axios.delete(url, {headers: headers});
    }

    authenticateLogin(credentials) {
        const url = `${API_URL}/api/`;
        return axios.post(url, credentials);
    }

    registerUser(credentials) {
        const url = `${API_URL}/register/`;
        credentials.guestname = credentials.username
        return axios.post(url, credentials);
    }
}
