import { defineStore } from 'pinia';
import { ref } from 'vue';


export const useUserStore = defineStore('user',
    () => {
        const user = ref(null);

        function setUser(userProfile) {
            // TODO: fix roles
            //const role;

            user.value = {
                username: userProfile.user,
                email: userProfile.email,
                firstname: userProfile.first_name,
                lastname: userProfile.last_name,
                document_type: userProfile.document_type,
                document_number: userProfile.document_number,
                address: userProfile.address,
                phone: userProfile.phone,
                gender: userProfile.gender,
                gender_other: userProfile.gender_other,
                //is_site_admin: isSiteAdmin,
                //is_institution_owner: isInstitutionOwner
            };
        }

        function clearUser() {
        user.value = null;
        }

        return { user, setUser, clearUser };
    },
    {
        persist: true
    }
);
