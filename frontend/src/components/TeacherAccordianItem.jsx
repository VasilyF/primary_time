import {
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box
} from '@chakra-ui/react';

import { Button } from '@chakra-ui/react'
import TimeRangePicker from './TimeRangePicker'

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
