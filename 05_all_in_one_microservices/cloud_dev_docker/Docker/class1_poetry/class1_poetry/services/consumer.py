from aiokafka import AIOKafkaConsumer
import todo_pb2
from class1_poetry.database import *
from class1_poetry.services.todo_services import *

async def consume_todo(topic:str, bootstrap_servers:str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers = bootstrap_servers,
        group_id="todo-group")
    
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.value)
            todo_data = todo_pb2.Todo_proto()
            todo_data.ParseFromString(msg.value)
             # Deserialize Data
            get_data = todo_pb2.Todo_proto()
            get_data.ParseFromString(msg.value)
            print(f"Deserialize Data : ", {get_data.title , get_data.description})

            with get_Session() as session:
                add_todo = await create_todo(todo=get_data, session=session)
                print ("Added Data: ", add_todo)
                

    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
