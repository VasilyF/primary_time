if (typeof global.navigator === 'undefined') global.navigator = {};
import React, {Component} from 'react';
import {DayPilot, DayPilotCalendar} from "@daypilot/daypilot-lite-react";


class Calendar extends Component {

    constructor(props) {
        super(props);

        this.calendarRef = React.createRef();

        this.state = {
            viewType: "Week",
            timeRangeSelectedHandling: "Enabled",
            onEventClick: async args => {
                const modal = await DayPilot.Modal.prompt("Update event text:", args.e.text());
                if (!modal.result) { return; }
                const e = args.e;
                e.data.text = modal.result;
                this.calendar.events.update(e);
            },
        };
    }

    calendar() {
        return this.calendarRef.current.control;
    }

    componentDidMount() {

        // load event data
        this.setState({
            startDate: "2022-09-07",
            events: [
                {
                    id: 1,
                    text: "Event 1",
                    start: "2022-09-07T10:30:00",
                    end: "2022-09-07T13:00:00"
                },
                {
                    id: 2,
                    text: "Event 2",
                    start: "2022-09-08T09:30:00",
                    end: "2022-09-08T11:30:00",
                    barColor: "#6aa84f"
                },
            ]
        });

    }

    render() {
        return (
            <DayPilotCalendar
                {...this.state}
                ref={this.calendarRef}
            />
        );
    }
}

export default Calendar;
