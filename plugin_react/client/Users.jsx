// This file is part of Indico.UN.
// Copyright (C) 2019 - 2023 United Nations. All rights reserved.

import PropTypes from 'prop-types';
import React from 'react';
import {List} from 'semantic-ui-react';

// import 'indico/modules/search/client/js/components/ResultList.module.scss';
import './ResultList.module.scss'

export default function User({firstName, lastName, url}) {
  return (
    <div styleName="item">
      <List.Header styleName="header">
        <a href={url}>
          {lastName} {firstName}
        </a>
      </List.Header>
      <List.Description styleName="description">test</List.Description>
    </div>
  );
}

User.propTypes = {
  firstName: PropTypes.string.isRequired,
  lastName: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired,
};
