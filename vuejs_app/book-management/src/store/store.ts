// state.js
import { reactive } from 'vue';

const state = reactive({
  authenticated: false,
  user: null,
});

const setAuth = (auth:any) => {
  state.authenticated = auth;
};

const setUser = (user:any) => {
  state.user = user;
};

export { state, setAuth, setUser };