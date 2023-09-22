import * as base from '@jupyter-widgets/base';

import * as myWidget from './widget';
import { version } from './index';

const id = 'cccs-ipyaggrid:plugin';
const requires = [base.IJupyterWidgetRegistry];
const autoStart = true;

const activate = (app, widgets) => {
    console.log('JupyterLab extension cccs-ipyaggrid is activated!');

    widgets.registerWidget({
        name: 'cccs-ipyaggrid',
        version,
        exports: myWidget,
    });
};

export default {
    id,
    requires,
    activate,
    autoStart,
};
