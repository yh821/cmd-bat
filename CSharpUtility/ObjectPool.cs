using System;
using System.Collections.Generic;

public class ObjectPool<T> where T : new()
{
    private readonly Stack<T> mStack = new Stack<T>();
    private readonly Action<T> mOnRelease;

    public ObjectPool(Action<T> onRelease)
    {
        mOnRelease = onRelease;
    }

    public T Get()
    {
        T t;
        if(mStack.Count==0)
            t = new T();
        else
            t = mStack.Pop();
        return t;
    }

    public Release(T t){
        if(mStack.Count>0 && mStack.Peek()==t)
            Debug.LogError("Internal error. Trying to destroy object that is already released to pool.");
        if(mOnRelease!=null)
            mOnRelease(t);
        mStack.Push(t);
    }

}