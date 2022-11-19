import {
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box
} from '@chakra-ui/react';

export default function TeachersAccordian(){
  return (
	<Accordion allowToggle>
	  <AccordionItem>
	    <h2>
	      <AccordionButton>
		<Box flex='1' textAlign='left'>
	  	  Jane Doe
		</Box>
		<AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	  	TODO: creating teacher-specific schedules
	    </AccordionPanel>
	  </AccordionItem>

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
	  	TODO: creating teacher-specific schedules
	    </AccordionPanel>
	  </AccordionItem>
	</Accordion>
  );
}
