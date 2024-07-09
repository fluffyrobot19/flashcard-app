## Modern JS

#### What is ECMAScript? What is the difference between Javascript & ECMAScript?
#### Explain the concept of "block scoping" introduced in ES6. How does it differ from function scoping?
#### What are template literals in ES6 and how do they improve string manipulation in JavaScript?
#### Explain the concept of "destructuring assignment" in ES6. How does it simplify variable assignment and object/array manipulation.
#### What is the "spread operator" in ES6 and how can it be used to manipulate arrays and objects more effectively?
#### How does ES6 introduce the concept of "default function parameters"? Provide an example of using default parameters in a function.
#### Explain the concept of "modules" introduced in ES6. How do they improve code organization and reusability in JavaScript?
#### Compare the CommonJS and ES6 "modules". What are the differences?
#### What are higher-order functions in JavaScript?
#### Explain the purpose and functionality of the map function in JavaScript. How does it differ from the filter and reduce functions?
#### How can the filter function be used to selectively extract elements from an array based on a given condition? Provide an example where the filter function is used to create a new array with only the elements that meet the specified criteria.
#### What is the role of the reduce function in JavaScript? How can it be used to aggregate or combine the elements of an array into a single value? Provide an example where the reduce function is used to calculate a cumulative sum or find the maximum value in an array.

## Fetch

#### How does a query string parameter in a URL contribute to web application functionality? Explain how query string parameters are typically used to pass data between web pages or APIs.
#### What is the purpose and functionality of the fetch function in JavaScript?
#### Explain the syntax of the fetch function and how it handles asynchronous operations. Compare and contrast the syntax of making HTTP requests using fetch with async/await versus the syntax using .then() and .catch(). What are the key differences and benefits of using the async/await syntax in terms of code structure and readability?
#### What is asynchronicity in JavaScript? Name some typical use cases when asynchronicity is needed.
#### How can you handle the response received from a fetch request?
#### How does the fetch function handle errors and handle HTTP status codes? Provide an example of using fetch to handle different types of responses, including successful and error responses.
#### Explain the parts of an URL.

## Serve

#### Explain the concept of client-server communication in the context of web development. How does information flow between the client and the server in a typical client-server architecture?
#### What is the role of HTTP requests and responses in web development? Explain the structure of an HTTP request and an HTTP response.
#### Explain the key differences between the CommonJS require syntax and the ECMAScript (ES) module syntax import. How do these two approaches handle module dependencies and exports in JavaScript?
#### What are the advantages of using the ES module syntax import over the CommonJS require syntax?
#### What is Express.js and how does it simplify web application development in Node.js? Explain the core features and benefits of using Express.js as a web framework.
#### Explain the process of handling static files (e.g., CSS, images) in Express.js. How can you configure Express.js to serve static assets from a specific directory in your application?
#### How does Express.js handle HTTP request/response cycles? Explain the process of receiving and responding to requests using Express.js middleware and route handlers.

## Forms

#### How does routing work in Express.js? Explain how to define routes and handle different HTTP methods (GET, POST, etc.) in an Express.js application.
#### What are the various methods available in Express.js for sending responses to clients? Explain the differences between res.send() and res.json[] in Express.js.
#### Explain what the express.json() middleware does?
#### What is the purpose of the next() function in Express.js middleware? How can you use it to pass control to the next middleware function in the chain or to terminate the middleware processing?
#### Explain the concept of route parameters in Express.js. How can you extract dynamic values from the URL path using route parameters, and how are these values accessed within route handlers?
#### Can you name some typical HTTP response codes and their meaning?
#### Can you name some typical HTTP request/response headers and their meaning?
#### What are the common HTTP methods used in web development, and what are their respective purposes?
#### How does the GET method differ from the POST method? Explain when it is appropriate to use each method. Which one uses request body to send data? What the other method uses to send data?
#### Explain the use of the PATCH method in HTTP. How does it differ from the PUT method, and when should it be used to update a resource?
#### How can the DELETE method be used to remove a resource from a server? Explain how the DELETE method works and any considerations for handling resource deletion.
#### How do you handle form submissions using JavaScript? Explain the process of capturing form data and preventing the default form submission behavior.
#### Explain the required elements necessary to define a form in HTML.
#### What is the purpose of the required attribute in HTML form elements? How does it enforce mandatory input fields and prevent form submission without the required information?
#### Explain the different types of form input fields available in HTML. How do input types like text, number, email, checkbox, and radio buttons differ, and how are they used in forms?
#### Can you explain the purpose of the name attribute in a context of form submission?
#### Can you explain how we can connect a label tag to a form element?
#### How can you dynamically manipulate or modify form elements using JavaScript? Explain how to add or remove form fields dynamically based on user interaction or specific conditions.
#### How can you convert form data into a format that can be easily transmitted or processed by the server?

## React

#### What is React.js and what are its key features?
#### Explain the concept of virtual DOM and how it contributes to React's performance.
#### Explain the component-based architecture in React.js. How do components work, and how can they be composed to build complex user interfaces?
#### What is the significance of JSX in React.js? Explain how JSX combines HTML-like syntax with JavaScript code and how it is transpiled into regular JavaScript during the build process.
#### What are props in React and how are they used to pass data between components? Explain the concept of props and how they facilitate parent-child component communication.
#### How can you access and utilize props within a functional component in React? Explain how to extract and use props using the destructuring syntax.
#### How can you pass callback functions as props in React? Provide an example of how to pass a function from a parent component to a child component, enabling the child to communicate with the parent.
#### Explain the concept of spreading props in React. How can the spread operator be used to pass multiple props from a parent component to a child component in a concise manner?
#### Explain the concept of default props (with ES6 JS syntax) in React. How can you define default values for props in a component to handle cases where the prop value is not explicitly passed?
#### Explain the immutability principle when working with props and states in React. Why is it important to avoid directly modifying prop values within a component, and what are some best practices for maintaining immutability?
#### How does React.js handle state management? Explain the concept of state and how it differs from props.
#### What are React hooks? Explain the purpose and benefits of hooks like useState, useEffect in React.js.
#### Explain the concept of virtual DOM reconciliation in React.js. How does React efficiently update and render components by performing minimal DOM manipulations?
#### Explain how to manage complex state objects with useState. Explain techniques like object spreading or merging to update specific properties within an object state.
#### Why is it important to provide a new array as an argument to the useState hook when adding an item to an existing array?
#### How does conditional rendering work in React? Explain the different techniques and approaches available to conditionally render components or content based on certain conditions or state values.  How can it be used to control the visibility or behavior of components based on user interactions or other dynamic conditions?
#### How can you create a select input element in React? How does it differ from the html's select tag? Can you show an example of a controlled and an uncontrolled select element with default value setting?

## Database

#### What is MongoDB, and how does it differ from traditional relational databases? Explain the key features and advantages of MongoDB as a NoSQL database solution.
#### Explain the concept of collections and documents in MongoDB? How does MongoDB store data, and how is it organized within collections and documents.
#### What is Mongoose.js, and how does it simplify working with MongoDB in a Node.js environment? Explain the key features and benefits of using Mongoose.js.
#### How do you define and create schemas in Mongoose.js? Explain how schemas define the structure and validation rules for documents in MongoDB collections.
#### Explain the different types of Mongoose.js data modeling techniques. How can you define relationships between MongoDB collections using Mongoose.js, such as one-to-one, one-to-many, and many-to-many relationships?
#### What are the available options for querying and manipulating data using Mongoose.js? Explain how to perform CRUD operations (create, read, update, delete) using Mongoose.js methods and queries.
#### Explain the process of connecting to a MongoDB database using Mongoose.js. How can you configure and establish a connection to a MongoDB server using Mongoose.js in a Node.js application?

## MERN

#### Explain the concept of React Router. How does it enable client-side routing in React.js applications and facilitate the creation of multi-page-like experiences?
#### Explain the concept of server-side routing in Express.js. How does Express handle incoming requests and route them to the appropriate API endpoints or route handlers?
#### What is the MERN stack? Explain the individual components of the MERN stack and their role in building web applications.
#### Explain how does a proxy works during React development. How can you tell the webpack dev server to proxy the requests to your backend? What kind of URLs you have to use in the fetch in your JS code, if you want to use the proxy.
#### Explain the advantages and benefits of using the MERN stack for web development. How does each component of the MERN stack contribute to the development process and overall efficiency of building modern web applications?
#### How does data flow in the MERN stack architecture? Explain how the frontend, built with React.js, communicates with the backend, developed with Node.js and Express.js, to handle client requests and serve data from the MongoDB database.
END OF FILE