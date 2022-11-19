import { TimePicker, Select } from 'antd'

export default function TimeRangePicker(){
  return (
	  <span>
	      <Select 
	         style={{ width: 100 }} 
	         options={[
	           {label: 'MON', value: 'MON'},
	           {label: 'TUES', value: 'TUES'},
	           {label: 'WED', value: 'WED'},
	           {label: 'THURS', value: 'THURS'},
	           {label: 'FRI', value: 'FRI'},
	         ]}
	      />	
	      <TimePicker.RangePicker />
	  </span>
  );
}
