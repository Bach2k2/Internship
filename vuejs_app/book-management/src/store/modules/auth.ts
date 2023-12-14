const state = {
    authenticated: false,
    user: null
};
const mutations = {
    SET_AUTH: (state: { authenticated: boolean }, auth: boolean) => { } ;
    // SET_USER(state: any, user: any) {
    //     state.user = user;
    // }
};
const actions = {
    // setAuth: ({ commit }: { commit: Commit }, auth: boolean) => commit('SET_AUTH', auth),
    // logout({ commit }: { commit: Commit }) {
    //     // Perform logout logic
    //     commit('SET_AUTHENTICATED', false);
    //     commit('SET_USER', null);
    // },
},
const getters = {

}
export default {
    state,
    mutations,
    actions,
    getters,
};