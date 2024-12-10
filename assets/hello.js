// assets/hello.js
import React from "react";
import { useState } from "react";

const Console = (prop) => (
  console[Object.keys(prop)[0]](...Object.values(prop)), null // ➜ React components must return something
);

export function Hello({ onSuccess, ...props }) {
  const [count1, setCount1] = useState(10);
  //const [ival, setIval] = useState("hernad");

  //function handleChange(e) {
  //  setIval(e.target.value);
  //}
  //const onChangeRef = useRef(onChange);
  //onChangeRef.current = onChange;

  const onSuccessHandler = onSuccess;

  const incrementCount1 = () => {
    setCount1((c) => {
      //console.error("setCount1");
      console.log("setCount1", c);
      c = c + 1;
      onSuccessHandler({ value: c }, "test");
      return c;
    });
  };

  return (
    <div>
      {console.log("start hello component")}
      <h3>Hello {props.user}!</h3>
      <div>
        Count: {count1}
        <button onClick={incrementCount1}>[ plus ]</button>
      </div>
    </div>
  );
}
