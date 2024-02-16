import { Component } from "react";
import { gantt } from 'dhtmlx-gantt';
import 'dhtmlx-gantt/codebase/dhtmlxgantt.css';
import './Gantt.css';
import './PARAM_GANTT.css';

export default class Gantt extends Component {

    constructor(props) {
        super(props);
        this.dataBase = this.props['tasks']; // database data
        this.ganttInitialState = null;
    };

    componentDidMount() {

        // initialize gantt editor and set constructor date boundaries
        if (!this.ganttInitialState) {
            this.ganttInitialState = gantt.getState();
        }

        // set the payload (tasks) in the library 
        const { tasks: payload } = this.props;

        gantt.render() // Renders UI

        gantt.init("gantt_here");  // Initialize the Gantt

        gantt.parse(payload); // Parse Gantt data

    }

    componentDidUpdate() {
        gantt.render();
    }


}
