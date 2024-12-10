// assets/hello.js
import React from "react";
import { useState, useRef } from "react";

const Console = (prop) => (
  console[Object.keys(prop)[0]](...Object.values(prop)), null // ➜ React components must return something
);

export function Hello({ onChange, ...props }) {
  const [count, setCount] = useState(10);
  const [ival, setIval] = useState("hernad");

  function handleChange(e) {
    setIval(e.target.value);
  }
  //const onChangeRef = useRef(onChange);
  //onChangeRef.current = onChange;
  const increment = () => {
    setCount((c) => {
      c = c + 1;
      return c;
    });
  };

  return (
    <div>
      <h3>Hello {props.user}!</h3>
      <div>
        Count: {count}
        <button onClick={increment}>[ + ]</button>
        <input onChange={onChange} />
        ival: {ival}
      </div>
    </div>
  );
}
