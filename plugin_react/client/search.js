import {registerPluginObject} from 'indico/utils/plugins';
import User from './Users';

//import {useSearch} from '../../../indico/indico/modules/search/client/js/components/SearchApp'
//import searchURL from 'indico-url:search.api_search';


registerPluginObject('un', 'search_result_types', ['Users', 'user', User]);
