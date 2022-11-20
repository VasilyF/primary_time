import {
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box,
  Button, 
  FormControl, 
  FormLabel, 
  Switch,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
} from '@chakra-ui/react';

import TimeRangePicker from './TimeRangePicker'
import SliderInput from './SliderInput'

export default function TeacherAccordianItem(){
  return (
  <AccordionItem>
    <h2>
      <AccordionButton>
	<Box flex='1' textAlign='left'>
	  John Doe
	</Box>
	<AccordionIcon />
      </AccordionButton>
    </h2>
    <AccordionPanel pb={4}>


      <div> 
        <SliderInput /> 
      </div>


      <FormControl display='flex' alignItems='center'>
         <FormLabel htmlFor='is_prep' mb='0'>
	  Is Prep Teacher: 
         </FormLabel>
         <Switch id='is_prep' />
      </FormControl>



      <div>
        <Button colorScheme='teal' variant='ghost'>
          Working
        </Button>
      </div>
      <TimeRangePicker />
      <div>
        <Button colorScheme='teal' variant='ghost'>
          Unscheduled
        </Button>
      </div>
      <TimeRangePicker />
    </AccordionPanel>
  </AccordionItem>
  );
}

