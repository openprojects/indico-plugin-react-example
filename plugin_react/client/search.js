// This file is part of Indico.UN.
// Copyright (C) 2019 - 2023 United Nations. All rights reserved.

import {registerPluginObject} from 'indico/utils/plugins';

import {Translate} from 'indico/react/i18n';
import User from './Users';

//import {useSearch} from '../../../indico/indico/modules/search/client/js/components/SearchApp'
//import searchURL from 'indico-url:search.api_search';


const searchResultsFromHooks = (
  [userResults, setUserPage] = 'user'
);

registerPluginObject('un', 'search_hooks', searchResultsFromHooks);


const resultRenderer = (
  [Translate.string('Users'), userResults, setUserPage, User]
);

registerPluginObject('un', 'search_map_entries', resultRenderer);
