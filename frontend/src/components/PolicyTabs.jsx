import {ChakraProvider} from "@chakra-ui/react";
import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/react'

import TeachersAccordian from './TeachersAccordian'

export default function PolicyTabs(){
  return (
      <ChakraProvider>
	<Tabs variant='enclosed'>
	  <TabList>
	    <Tab>School-wide</Tab>
	    <Tab>Teachers</Tab>
	  </TabList>
	  <TabPanels>
	    <TabPanel>
	      <p>TODO</p>
	    </TabPanel>
	    <TabPanel>
	      <TeachersAccordian />
	    </TabPanel>
	  </TabPanels>
	</Tabs>
      </ChakraProvider>
  );
}
